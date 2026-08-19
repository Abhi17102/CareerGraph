from app.database.cogno import driver


def seed_database():
    with driver.session() as session:
        print("Seeding CareerGraph database...")

        roles = [
            {
                "name": "Python Backend Developer",
                "description": "Builds backend services and APIs using Python."
            },
            {
                "name": "Full Stack Developer",
                "description": "Builds both frontend and backend web applications."
            },
            {
                "name": "Data Engineer",
                "description": "Builds systems for collecting, processing and managing data."
            },
            {
                "name": "AI Engineer",
                "description": "Builds applications using machine learning and AI technologies."
            },
            {
                "name": "ML Engineer",
                "description": "Develops and deploys machine learning models."
            },
            {
                "name": "Frontend Developer",
                "description": "Builds user interfaces and frontend web applications."
            },
        ]

        for role in roles:
            session.run(
                """
                MERGE (r:Role {name: $name})
                SET r.description = $description
                """,
                name=role["name"],
                description=role["description"],
            )
        skills = [
            {"name": "Python", "category": "Programming"},
            {"name": "SQL", "category": "Database"},
            {"name": "REST APIs", "category": "Backend"},
            {"name": "Async Programming", "category": "Backend"},
            {"name": "Database Design", "category": "Database"},
            {"name": "Data Structures", "category": "Computer Science"},
            {"name": "Git", "category": "Development Tools"},
            {"name": "Testing", "category": "Software Engineering"},
            {"name": "JavaScript", "category": "Programming"},
            {"name": "HTML/CSS", "category": "Frontend"},
            {"name": "Data Analysis", "category": "Data"},
            {"name": "Machine Learning", "category": "AI"},
            {"name": "Deep Learning", "category": "AI"},
            {"name": "Statistics", "category": "Data"},
            {"name": "Docker", "category": "DevOps"},
            {"name": "Cloud Computing", "category": "Cloud"},
            {"name": "System Design", "category": "Software Engineering"},
        ]

        for skill in skills:
            session.run(
                """
                MERGE (s:Skill {name: $name})
                SET s.category = $category
                """,
                name=skill["name"],
                category=skill["category"],
            )

        technologies = [
            {"name": "FastAPI", "type": "Backend Framework"},
            {"name": "Django", "type": "Backend Framework"},
            {"name": "PostgreSQL", "type": "Database"},
            {"name": "Redis", "type": "Database"},
            {"name": "React", "type": "Frontend Framework"},
            {"name": "Node.js", "type": "Runtime"},
            {"name": "Pandas", "type": "Data"},
            {"name": "NumPy", "type": "Data"},
            {"name": "TensorFlow", "type": "Machine Learning"},
            {"name": "PyTorch", "type": "Machine Learning"},
            {"name": "Docker", "type": "DevOps"},
            {"name": "AWS", "type": "Cloud"},
        ]

        for technology in technologies:
            session.run(
                """
                MERGE (t:Technology {name: $name})
                SET t.type = $type
                """,
                name=technology["name"],
                type=technology["type"],
            )

        projects = [
            {
                "name": "E-Commerce API",
                "description": "Backend API for an online shopping platform."
            },
            {
                "name": "AI Document Analyzer",
                "description": "Application that analyzes and extracts information from documents."
            },
            {
                "name": "Analytics Dashboard",
                "description": "Dashboard for exploring business and operational data."
            },
            {
                "name": "Job Matching Platform",
                "description": "Platform that connects candidates with suitable job opportunities."
            },
            {
                "name": "Recommendation Engine",
                "description": "System that generates personalized recommendations."
            },
            {
                "name": "Developer Portfolio Website",
                "description": "Responsive portfolio website showcasing projects, skills and professional experience."
            },
            {
                "name": "E-Commerce Frontend",
                "description": "Interactive web interface for browsing products, managing carts and completing purchases."
            },
            {
                "name": "Real-Time Chat Application",
                "description": "Web application that enables users to communicate through real-time messaging."
            },
            {
                "name": "Data Pipeline Platform",
                "description": "Pipeline for collecting, transforming and loading data into analytical systems."
            },
            {
                "name": "Fraud Detection System",
                "description": "Machine learning system that identifies potentially fraudulent transactions."
            },
            {
                "name": "ML Model Serving API",
                "description": "Production API for serving machine learning predictions to applications."
            },
        ]

        for project in projects:
            session.run(
                """
                MERGE (p:Project {name: $name})
                SET p.description = $description
                """,
                name=project["name"],
                description=project["description"],
            )

        role_skills = {
            "Python Backend Developer": [
                "Python",
                "SQL",
                "REST APIs",
                "Async Programming",
                "Database Design",
                "Git",
                "Testing",
            ],

            "Full Stack Developer": [
                "Python",
                "JavaScript",
                "HTML/CSS",
                "SQL",
                "REST APIs",
                "Git",
                "Testing",
            ],

            "Data Engineer": [
                "Python",
                "SQL",
                "Data Analysis",
                "Database Design",
                "Docker",
                "Cloud Computing",
            ],

            "AI Engineer": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "Statistics",
                "Data Analysis",
                "REST APIs",
                "Cloud Computing",
            ],

            "ML Engineer": [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "Statistics",
                "Data Analysis",
                "Docker",
            ],

            "Frontend Developer": [
                "JavaScript",
                "HTML/CSS",
                "Git",
                "Testing",
            ],
        }

        for role_name, skill_names in role_skills.items():
            for skill_name in skill_names:
                session.run(
                    """
                    MATCH (r:Role {name: $role_name})
                    MATCH (s:Skill {name: $skill_name})
                    MERGE (r)-[:REQUIRES]->(s)
                    """,
                    role_name=role_name,
                    skill_name=skill_name,
                )

        related_skills = [
            ("Python", "Async Programming"),
            ("Python", "Data Analysis"),
            ("Python", "Machine Learning"),

            ("SQL", "Database Design"),
            ("SQL", "Data Analysis"),

            ("Machine Learning", "Deep Learning"),
            ("Machine Learning", "Statistics"),

            ("Data Analysis", "Statistics"),

            ("REST APIs", "Async Programming"),
            ("REST APIs", "System Design"),

            ("Docker", "Cloud Computing"),

            ("JavaScript", "HTML/CSS"),
        ]

        for skill_a, skill_b in related_skills:
            session.run(
                """
                MATCH (a:Skill {name: $skill_a})
                MATCH (b:Skill {name: $skill_b})
                MERGE (a)-[:RELATED_TO]->(b)
                """,
                skill_a=skill_a,
                skill_b=skill_b,
            )

        skill_technologies = [
            ("Python", "FastAPI"),
            ("Python", "Django"),

            ("SQL", "PostgreSQL"),
            ("SQL", "Redis"),

            ("JavaScript", "React"),
            ("JavaScript", "Node.js"),

            ("Data Analysis", "Pandas"),
            ("Data Analysis", "NumPy"),

            ("Machine Learning", "TensorFlow"),
            ("Machine Learning", "PyTorch"),

            ("Docker", "Docker"),

            ("Cloud Computing", "AWS"),
        ]

        for skill_name, technology_name in skill_technologies:
            session.run(
                """
                MATCH (s:Skill {name: $skill_name})
                MATCH (t:Technology {name: $technology_name})
                MERGE (s)-[:IMPLEMENTED_BY]->(t)
                """,
                skill_name=skill_name,
                technology_name=technology_name,
            )

        project_technologies = [
            # E-Commerce API
            ("E-Commerce API", "FastAPI"),
            ("E-Commerce API", "PostgreSQL"),

        # AI Document Analyzer
            ("AI Document Analyzer", "FastAPI"),
            ("AI Document Analyzer", "TensorFlow"),
            ("AI Document Analyzer", "AWS"),

        # Analytics Dashboard
            ("Analytics Dashboard", "Pandas"),
            ("Analytics Dashboard", "NumPy"),
            ("Analytics Dashboard", "PostgreSQL"),

            # Job Matching Platform
            ("Job Matching Platform", "FastAPI"),
            ("Job Matching Platform", "PostgreSQL"),

            # Recommendation Engine
            ("Recommendation Engine", "PyTorch"),

        # Developer Portfolio Website
            ("Developer Portfolio Website", "React"),

        # E-Commerce Frontend
            ("E-Commerce Frontend", "React"),
            ("E-Commerce Frontend", "Node.js"),

        # Real-Time Chat Application
            ("Real-Time Chat Application", "React"),
            ("Real-Time Chat Application", "Node.js"),
            ("Real-Time Chat Application", "Redis"),

        # Data Pipeline Platform
            ("Data Pipeline Platform", "Pandas"),
            ("Data Pipeline Platform", "NumPy"),
            ("Data Pipeline Platform", "AWS"),
            ("Data Pipeline Platform", "Docker"),

        # Fraud Detection System
            ("Fraud Detection System", "Pandas"),
            ("Fraud Detection System", "PyTorch"),

        # ML Model Serving API
            ("ML Model Serving API", "FastAPI"),
            ("ML Model Serving API", "Docker"),
            ("ML Model Serving API", "AWS"),
        ]

        for project_name, technology_name in project_technologies:
            session.run(
                """
                MATCH (p:Project {name: $project_name})
                MATCH (t:Technology {name: $technology_name})
                MERGE (p)-[:USES]->(t)
                """,
                project_name=project_name,
                technology_name=technology_name,
            )

        project_skills = [
        # E-Commerce API
            ("E-Commerce API", "Python"),
            ("E-Commerce API", "REST APIs"),
            ("E-Commerce API", "SQL"),
            ("E-Commerce API", "Database Design"),
            ("E-Commerce API", "Testing"),

        # AI Document Analyzer
            ("AI Document Analyzer", "Python"),
            ("AI Document Analyzer", "Machine Learning"),
            ("AI Document Analyzer", "Deep Learning"),
            ("AI Document Analyzer", "Data Analysis"),

        # Analytics Dashboard
            ("Analytics Dashboard", "Python"),
            ("Analytics Dashboard", "Data Analysis"),
            ("Analytics Dashboard", "SQL"),

        # Job Matching Platform
            ("Job Matching Platform", "Python"),
            ("Job Matching Platform", "REST APIs"),
            ("Job Matching Platform", "Database Design"),

        # Recommendation Engine
            ("Recommendation Engine", "Python"),
            ("Recommendation Engine", "Machine Learning"),
            ("Recommendation Engine", "Statistics"),

        # Developer Portfolio Website
            ("Developer Portfolio Website", "JavaScript"),
            ("Developer Portfolio Website", "HTML/CSS"),
            ("Developer Portfolio Website", "Git"),

        # E-Commerce Frontend
            ("E-Commerce Frontend", "JavaScript"),
            ("E-Commerce Frontend", "HTML/CSS"),
            ("E-Commerce Frontend", "Git"),
            ("E-Commerce Frontend", "Testing"),

        # Real-Time Chat Application
            ("Real-Time Chat Application", "JavaScript"),
            ("Real-Time Chat Application", "HTML/CSS"),
            ("Real-Time Chat Application", "REST APIs"),
            ("Real-Time Chat Application", "Testing"),

        # Data Pipeline Platform
            ("Data Pipeline Platform", "Python"),
            ("Data Pipeline Platform", "SQL"),
            ("Data Pipeline Platform", "Data Analysis"),
            ("Data Pipeline Platform", "Docker"),
            ("Data Pipeline Platform", "Cloud Computing"),

        # Fraud Detection System
            ("Fraud Detection System", "Python"),
            ("Fraud Detection System", "Machine Learning"),
            ("Fraud Detection System", "Statistics"),
            ("Fraud Detection System", "Data Analysis"),

        # ML Model Serving API
            ("ML Model Serving API", "Python"),
            ("ML Model Serving API", "Machine Learning"),
            ("ML Model Serving API", "REST APIs"),
            ("ML Model Serving API", "Docker"),
            ("ML Model Serving API", "Cloud Computing"),
        ]

        for project_name, skill_name in project_skills:
            session.run(
                """
                MATCH (p:Project {name: $project_name})
                MATCH (s:Skill {name: $skill_name})
                MERGE (p)-[:DEMONSTRATES]->(s)
                """,
                project_name=project_name,
                skill_name=skill_name,
            )

if __name__ == "__main__":
    try:
        seed_database()
        print("Database seeded successfully")
    except Exception as e:
        print(f"Seeding failed: {e}")
    finally:
        driver.close()