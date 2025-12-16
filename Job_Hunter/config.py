class JobSearchConfig:
    # -------------------
    # Títulos de vagas
    # -------------------
    JOB_TITLES = [
        "Software Architect",
        "Senior .NET Developer",
        "ASP.NET Core Developer",
        "C# Developer",
        "Flutter Developer",
        "Senior Backend Developer",
        "Full Stack Developer",
        "Cloud Architect",
        "AI Developer",
        "Lead Software Engineer",
        "DevOps Engineer",
        "Mobile Developer",
        "Technical Lead",
        "Solution Architect"
    ]

    # -------------------
    # Localizações
    # -------------------
    LOCATIONS = [
        # Europa
        "Amsterdam, Netherlands", "Athens, Greece", "Barcelona, Spain", "Berlin, Germany",
        "Brussels, Belgium", "Budapest, Hungary", "Copenhagen, Denmark", "Dublin, Ireland",
        "Helsinki, Finland", "Lisbon, Portugal", "London, UK", "Luxembourg, Luxembourg",
        "Madrid, Spain", "Milan, Italy", "Munich, Germany", "Oslo, Norway", "Paris, France",
        "Prague, Czech Republic", "Rome, Italy", "Stockholm, Sweden", "Vienna, Austria",
        "Warsaw, Poland", "Zurich, Switzerland", "Bratislava, Slovakia", "Tallinn, Estonia",
        "Vilnius, Lithuania", "Riga, Latvia", "Reykjavik, Iceland", "Valletta, Malta",
        # EUA principais hubs
        "New York, USA", "San Francisco, USA", "Boston, USA", "Chicago, USA", "Seattle, USA",
        "Austin, USA", "Los Angeles, USA", "Washington DC, USA"
    ]

    # -------------------
    # Senioridade
    # -------------------
    SENIORITY_LEVELS = ["Senior", "Lead", "Architect", "Principal", "Staff"]

    # -------------------
    # Skills obrigatórias
    # -------------------
    SKILLS = [
        "C#", ".NET Core", "ASP.NET", "MVC", "Flutter", "React", "Angular",
        "Microservices", "Cloud", "AWS", "Azure", "GCP", "Docker", "Kubernetes",
        "AI", "Machine Learning", "DevOps", "CI/CD", "SQL", "NoSQL", "GraphQL", "REST"
    ]

    # -------------------
    # Stack / tipo de vaga
    # -------------------
    STACK_TYPE = [
        "Full Stack", "Backend", "Frontend", "Mobile", "Cloud", "AI", "DevOps", "Architect"
    ]

    # -------------------
    # Filtro de tempo (dias desde publicação)
    # -------------------
    MAX_DAYS_OLD = 3

    # -------------------
    # Filtro de prioridade (opcional: pode priorizar vagas remotas ou grandes empresas)
    # -------------------
    PRIORITY = {
        "remote_first": True,        # Prioriza vagas remotas
        "big_companies": ["Microsoft", "Google", "Amazon", "Meta", "IBM", "SAP", "Siemens", "Accenture"],
        "startups_only": False
    }
