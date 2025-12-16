import json
import csv
from pathlib import Path
from fetchers.linkedin_fetcher import LinkedInFetcher
from filters.job_filter import JobFilter
from notifications.telegram_notifier import TelegramNotifier
from utils.logger import setup_logger
from config import JobSearchConfig

logger = setup_logger()
CACHE_FILE = Path("data/jobs_cache.json")
OUTPUT_CSV = Path("data/jobs_list.csv")
OUTPUT_JSON = Path("data/jobs_list.json")

# -----------------------------
# Cache
# -----------------------------
def load_cache():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()
                if not data:
                    return set()
                return set(json.loads(data))
        except json.JSONDecodeError:
            return set()
    return set()

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(list(cache), f, ensure_ascii=False, indent=2)

# -----------------------------
# Salvar CSV
# -----------------------------
def save_csv(jobs):
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "URL"])
        for job in jobs:
            writer.writerow([job.title, job.company, job.location, job.url])

# -----------------------------
# Salvar JSON
# -----------------------------
def save_json(jobs):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump([{
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "url": job.url
        } for job in jobs], f, ensure_ascii=False, indent=2)

# -----------------------------
# Main
# -----------------------------
def main():
    sent_jobs = load_cache()
    all_jobs = []

    fetcher = LinkedInFetcher(max_jobs_per_search=50, headless=True)

    for title in JobSearchConfig.JOB_TITLES:
        for location in JobSearchConfig.LOCATIONS:
            try:
                jobs = fetcher.fetch(keywords=title, location=location)
                all_jobs.extend(jobs)
                logger.info(f"{len(jobs)} jobs fetched for '{title}' in {location}")
            except Exception as e:
                logger.error(f"Error fetching LinkedIn jobs for '{title}' in {location}: {e}")

    # Filtrar vagas
    job_filter = JobFilter(
        skills=JobSearchConfig.SKILLS,
        seniority=JobSearchConfig.SENIORITY_LEVELS,
        locations=JobSearchConfig.LOCATIONS,
        max_days_old=JobSearchConfig.MAX_DAYS_OLD
    )
    filtered_jobs = job_filter.filter_jobs(all_jobs)
    logger.info(f"{len(filtered_jobs)} jobs after filtering")

    # Enviar Telegram e atualizar cache
    notifier = TelegramNotifier(bot_token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID")
    new_jobs_count = 0
    for job in filtered_jobs:
        if job.url not in sent_jobs:
            message = f"{job.title} at {job.company} - {job.location}\n{job.url}"
            notifier.send_message(message)
            sent_jobs.add(job.url)
            new_jobs_count += 1
            logger.info(f"Sent job: {job.title} at {job.company}")

    save_cache(sent_jobs)
    logger.info(f"{new_jobs_count} new jobs sent today")

    save_csv(filtered_jobs)
    save_json(filtered_jobs)
    logger.info(f"Saved {len(filtered_jobs)} jobs to CSV and JSON")

if __name__ == "__main__":
    main()
