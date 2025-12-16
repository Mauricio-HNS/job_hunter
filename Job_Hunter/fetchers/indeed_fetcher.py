import requests
from models.job import Job
from datetime import datetime

class IndeedFetcher:
    BASE_URL = "https://www.indeed.com/jobs"

    def fetch(self, keywords="C# .NET Core Flutter React", location="Madrid"):
        jobs = []
        params = {
            "q": keywords,
            "l": location,
            "fromage": "1",  # últimas 24h
            "sort": "date"
        }
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(self.BASE_URL, params=params, headers=headers)
        # Aqui você precisa implementar parsing HTML usando BeautifulSoup ou similar
        # Por enquanto, deixamos como lista vazia
        return jobs
