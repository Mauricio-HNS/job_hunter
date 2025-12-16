class JobFilter:
    def __init__(self, skills=None, seniority=None, locations=None, max_days_old=1):
        self.skills = skills or []
        self.seniority = seniority or []
        self.locations = locations or []
        self.max_days_old = max_days_old

    def filter_jobs(self, jobs):
        filtered = []
        for job in jobs:
            if self.skills and not any(skill.lower() in job.skills for skill in self.skills):
                continue
            if self.seniority and job.seniority not in self.seniority:
                continue
            if self.locations and job.location not in self.locations:
                continue
            if (datetime.now() - job.date_posted).days > self.max_days_old:
                continue
            filtered.append(job)
        return filtered
