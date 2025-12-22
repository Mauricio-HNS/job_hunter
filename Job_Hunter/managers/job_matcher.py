# Job_Hunter/managers/job_matcher.py
from Job_Hunter.models.job import Job

class JobMatcher:
    def __init__(self, min_compatibility=50):
        self.min_compatibility = min_compatibility

    def compute_compatibility(self, job, cv_data):
        """
        Calcula compatibilidade com base em skills (simples exemplo)
        """
        job_skills = getattr(job, "skills", []) or []
        cv_skills = cv_data.get("skills", [])

        if not job_skills:
            return 50  # padrão

        matched = sum(1 for skill in job_skills if skill.lower() in [s.lower() for s in cv_skills])
        return int((matched / len(job_skills)) * 100)

    def filter_jobs(self, jobs, cv_data):
        compatible_jobs = []
        for job in jobs:
            job.compatibility = self.compute_compatibility(job, cv_data)
            if job.compatibility >= self.min_compatibility:
                compatible_jobs.append(job)
        return compatible_jobs
