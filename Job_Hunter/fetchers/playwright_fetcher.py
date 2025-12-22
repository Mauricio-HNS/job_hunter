from playwright.sync_api import sync_playwright
from utils.logger import setup_logger
from models.job import Job
import time

logger = setup_logger()

class PlaywrightFetcher:
    def __init__(self, headless=True):
        self.headless = headless

    def fetch_google_jobs(self, title: str, location: str, max_results=20):
        """Busca vagas no Google Jobs e retorna uma lista de objetos Job"""
        jobs = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            context = browser.new_context()
            page = context.new_page()

            query = f"{title} jobs in {location}"
            page.goto(f"https://www.google.com/search?q={query.replace(' ', '+')}&ibp=htl;jobs")
            time.sleep(3)  # esperar página carregar
            
            cards = page.query_selector_all("div[jsname='t6HI6d']")  # Google Jobs card
            for card in cards[:max_results]:
                try:
                    job_title = card.query_selector("div[role='heading']").inner_text().strip()
                    company = card.query_selector("div[class*='vNEEBe']").inner_text().strip()
                    job_location = card.query_selector("div[class*='Qk80Jf']").inner_text().strip()
                    url_elem = card.query_selector("a[jsname='s5Q9Rc']")
                    url = url_elem.get_attribute("href") if url_elem else ""
                    jobs.append(Job(
                        title=job_title,
                        company=company,
                        location=job_location,
                        url=url,
                        skills=[]
                    ))
                except Exception as e:
                    logger.error(f"Error parsing job card: {e}")

            browser.close()

        logger.info(f"{len(jobs)} jobs fetched from Google Jobs for '{title}' in {location}")
        return jobs

    def fetch_job_description(self, url: str) -> str:
        """Abre a página da vaga e extrai todo o texto da descrição"""
        description = ""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            try:
                page.goto(url)
                time.sleep(2)
                # Ajuste o seletor de acordo com a página da vaga
                description = page.inner_text("div[jsname='lP2eKc']")
            except Exception as e:
                logger.error(f"Error fetching job description from {url}: {e}")
            finally:
                browser.close()
        return description
