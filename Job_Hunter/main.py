# Job_Hunter/main.py
from Job_Hunter.managers.cv_manager import CVManager
from Job_Hunter.managers.job_matcher import JobMatcher
from Job_Hunter.fetchers.linkedin_fetcher import LinkedInFetcher
from Job_Hunter.utils.logger import setup_logger

logger = setup_logger()

def main():
    cv_manager = CVManager()
    job_matcher = JobMatcher(min_compatibility=50)
    fetcher = LinkedInFetcher()

    # --- Simula upload do CV ---
    cv_data = cv_manager.upload_cv("data/cvs/meu_cv.pdf")
    logger.info(f"CV loaded: {cv_data}")

    # --- Buscar vagas ---
    jobs = fetcher.fetch(keywords="Software Architect", location="Lisbon, Portugal")
    logger.info(f"{len(jobs)} jobs fetched")

    # --- Filtrar compatíveis ---
    compatible_jobs = job_matcher.filter_jobs(jobs, cv_data)
    logger.info(f"{len(compatible_jobs)} jobs match the CV with >= {job_matcher.min_compatibility}% compatibility")

    return compatible_jobs

if __name__ == "__main__":
    main()
