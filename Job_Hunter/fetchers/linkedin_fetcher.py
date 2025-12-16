# Job_Hunter/fetchers/linkedin_fetcher.py
from playwright.sync_api import sync_playwright
from Job_Hunter.job import Job
import logging
import time

logger = logging.getLogger(__name__)

class LinkedInFetcher:
    BASE_URL = "https://www.linkedin.com/jobs/search/"

    def __init__(self):
        # Você pode configurar autenticação aqui, se necessário
        self.playwright = None
        self.browser = None

    def fetch(self, keywords, location, max_jobs=20):
        """
        Busca vagas no LinkedIn com base em palavras-chave e localização.
        Retorna uma lista de objetos Job.
        """
        jobs = []
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=True)
            page = self.browser.new_page()
            
            query = f"?keywords={keywords.replace(' ', '%20')}&location={location.replace(' ', '%20')}"
            url = self.BASE_URL + query
            logger.info(f"Navigating to LinkedIn Jobs: {url}")
            page.goto(url, timeout=60000)

            # Scroll para carregar mais vagas
            scroll_count = 0
            while len(jobs) < max_jobs and scroll_count < 10:
                page.mouse.wheel(0, 1000)
                time.sleep(1)
                scroll_count += 1

                # Seleciona as vagas carregadas
                job_elements = page.query_selector_all("ul.jobs-search__results-list li a.job-card-list__title")
                for elem in job_elements:
                    title = elem.inner_text().strip()
                    job_url = elem.get_attribute("href")
                    if job_url.startswith("/"):
                        job_url = "https://www.linkedin.com" + job_url
                    if not any(j.url == job_url for j in jobs):
                        jobs.append(Job(title=title, company=None, url=job_url, location=location))
                    if len(jobs) >= max_jobs:
                        break

            logger.info(f"LinkedInFetcher fetched {len(jobs)} jobs for '{keywords}' in {location}")
        except Exception as e:
            logger.error(f"Error in LinkedInFetcher: {e}")
        finally:
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()

        return jobs
