\# CareerGraph



CareerGraph is a graph-powered career exploration application that helps users understand how career roles connect to required skills, technologies, and real-world projects.



The project uses FastAPI for the backend and Neo4j as the graph database to model relationships between careers, skills, technologies, and projects.



\## Problem



Career information is often presented as disconnected lists of skills and technologies.



It can be difficult to understand:



\- Which skills are required for a career

\- Which technologies are associated with those skills

\- Which projects demonstrate those skills

\- How all of these concepts are connected



\## Solution



CareerGraph represents career information as a graph.



A career role is connected to its required skills, those skills connect to technologies, and projects connect back to the skills they demonstrate.



Example:



Role → Skills → Technologies



Role → Skills ← Projects



This allows users to explore career paths through relationships rather than isolated information.



\## Features



\- Explore available career roles

\- View required skills for each role

\- View related technologies

\- Find projects that demonstrate multiple required skills

\- Interactive career graph visualization

\- Graph relationships between roles, skills, technologies, and projects

\- REST API built with FastAPI

\- Neo4j graph database integration

\- Database error handling

\- Simple responsive web interface



\## Architecture



```text

&#x20;                   ┌─────────────────┐

&#x20;                   │   Web Frontend  │

&#x20;                   │ HTML/CSS/JS     │

&#x20;                   │   Cytoscape.js  │

&#x20;                   └────────┬────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌─────────────────┐

&#x20;                   │    FastAPI      │

&#x20;                   │      API        │

&#x20;                   └────────┬────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌─────────────────┐

&#x20;                   │ Service Layer   │

&#x20;                   │ Graph Queries   │

&#x20;                   └────────┬────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌─────────────────┐

&#x20;                   │     Neo4j       │

&#x20;                   │ Graph Database  │

&#x20;                   └─────────────────┘

````



\## Tech Stack



\### Backend



\* Python

\* FastAPI

\* Neo4j Python Driver

\* Pydantic Settings



\### Database



\* Neo4j

\* Cypher



\### Frontend



\* HTML

\* CSS

\* JavaScript

\* Cytoscape.js



\### Tools



\* Git

\* GitHub

\* Uvicorn



\## Graph Model



The application models relationships such as:



```text

(Role)

&#x20;  │

&#x20;  │ REQUIRES

&#x20;  ▼

(Skill)

&#x20;  │

&#x20;  │ IMPLEMENTED\_BY

&#x20;  ▼

(Technology)





(Project)

&#x20;  │

&#x20;  │ DEMONSTRATES

&#x20;  ▼

(Skill)

```



A role can require multiple skills.



A skill can be implemented using multiple technologies.



A project can demonstrate multiple skills.



Projects are surfaced when they demonstrate at least three skills required by the selected role.



\## API Endpoints



| Method | Endpoint                              | Description                        |

| ------ | ------------------------------------- | ---------------------------------- |

| GET    | `/health`                             | API health check                   |

| GET    | `/api/roles`                          | Get available career roles         |

| GET    | `/api/roles/{role\_name}/skills`       | Get skills required by a role      |

| GET    | `/api/roles/{role\_name}/technologies` | Get technologies related to a role |

| GET    | `/api/roles/{role\_name}/projects`     | Get projects matching the role     |

| GET    | `/api/roles/{role\_name}/graph`        | Get complete graph data            |



\## Project Structure



```text

CareerGraph/

│

├── app/

│   ├── database/

│   │   └── cogno.py

│   │

│   ├── routes/

│   │   └── graph.py

│   │

│   ├── services/

│   │   └── graph\_services.py

│   │

│   ├── config.py

│   └── main.py

│

├── scripts/

│   ├── seed.py

│   ├── test\_queries.py

│   └── test\_services.py

│

├── static/

│   ├── index.html

│   ├── style.css

│   └── app.js

│

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

```



\## How to Run Locally



\### 1. Clone the repository



```bash

git clone (https://github.com/Abhi17102/CareerGraph.git)

cd CareerGraph

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the environment



Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Configure environment variables



Create a `.env` file based on `.env.example`.



Add your Neo4j connection details:



```env

COGNODB\_URI=your\_neo4j\_uri

COGNODB\_USERNAME=your\_username

COGNODB\_PASSWORD=your\_password

```



Never commit `.env` to GitHub.



\### 6. Start the API



```bash

uvicorn app.main:app --reload

```



Open:



```text

http://127.0.0.1:8000

```



\## API Documentation



FastAPI automatically provides interactive API documentation.



Swagger UI:



```text

http://127.0.0.1:8000/docs

```



ReDoc:



```text

http://127.0.0.1:8000/redoc

```





\## Future Improvements



Possible future improvements include:



\* More career roles and datasets

\* Improved graph interactions

\* Career recommendation based on user skills

\* Skill-gap analysis

\* User profiles

\* Authentication

\* Deployment with a hosted Neo4j database



\## License



This project is intended as a portfolio and learning project.



````





