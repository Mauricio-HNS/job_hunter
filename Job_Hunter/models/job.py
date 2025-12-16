from datetime import datetime

class Job:
    def __init__(self, title, company, url, skills=None, location=None, seniority=None, date_posted=None):
        self.title = title
        self.company = company
        self.url = url
        self.skills = skills or []
        self.location = location
        self.seniority = seniority
        self.date_posted = date_posted or datetime.now()

    def __repr__(self):
        return f"<Job {self.title} at {self.company}>"
