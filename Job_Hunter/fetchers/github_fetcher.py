# fetchers/github_fetcher.py
import requests
from models.job import Job  # classe Job que você definiu no models/job.py
import logging

logger = logging.getLogger(__name__)

class GitHubFetcher:
    BASE_URL = "https://jobs.github.com/positions.json"  # endpoint oficial antigo da API GitHub Jobs

    def fetch(self, keywords=None, location=None):
        """
        Busca vagas no GitHub Jobs.
        :param keywords: string ou lista de palavras-chave
        :param location: cidade/país
        :return: lista de objetos Job
        """
        jobs = []
        try:
            params = {}
            if keywords:
                params["description"] = keywords
            if location:
                params["location"] = location

            response = requests.get(self.BASE_URL, params=params)
            if response.status_code != 200:
                logger.error(f"GitHub Jobs API returned {response.status_code}")
                return jobs

            data = response.json()
            for item in data:
                job = Job(
                    title=item.get("title"),
                    company=item.get("company"),
                    location=item.get("location"),
                    url=item.get("url"),
                    skills=item.get("tags", [])  # GitHub Jobs API não tem campo skills oficial, usar tags se disponível
                )
                jobs.append(job)

        except Exception as e:
            logger.error(f"Error fetching GitHub jobs: {e}")

        return jobs
