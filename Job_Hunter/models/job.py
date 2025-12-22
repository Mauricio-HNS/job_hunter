# Job_Hunter/models/job.py
class Job:
    def __init__(self, title, company=None, url=None, location=None, compatibility=None):
        self.title = title
        self.company = company
        self.url = url
        self.location = location
        self.compatibility = compatibility
        self.applied = False  # Para botão "Aplicar"
