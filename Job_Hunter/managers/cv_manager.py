# Job_Hunter/managers/cv_manager.py
from Job_Hunter.utils.cv_parser import parse_cv

class CVManager:
    def upload_cv(self, file_path):
        """
        Simula o upload do CV e retorna os dados estruturados do CV
        """
        cv_data = parse_cv(file_path)
        return cv_data
