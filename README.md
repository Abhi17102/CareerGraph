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

## Why a Graph Database?

CareerGraph focuses on relationships between career roles, skills, technologies, and projects.

A relational database could store these entities in separate tables, but exploring their relationships would require multiple joins across tables.

A graph database makes these connections first-class relationships.

For example:

Role → REQUIRES → Skill → IMPLEMENTED_BY → Technology

and:

Project → DEMONSTRATES → Skill ← REQUIRES ← Role

This makes multi-hop relationship queries and discovering connected career information more natural and easier to extend.

For CareerGraph, the graph model is useful because the main questions are relationship-oriented, such as:

- What skills does a career require?
- Which technologies implement those skills?
- Which projects demonstrate multiple skills required by a role?
- How are a career, its skills, technologies, and projects connected?

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



## Graph Data Model

CareerGraph uses the following graph model:

```text
                 REQUIRES
        ┌─────────────────────┐
        │                     ▼
     (Role)                (Skill)
                              │
                              │ IMPLEMENTED_BY
                              ▼
                        (Technology)

     (Project)
         │
         │ DEMONSTRATES
         ▼
       (Skill)

Nodes
Role
name
description
Skill
name
category
Technology
name
type
Project
name
description
Relationships
Role -[:REQUIRES]-> Skill
Skill -[:IMPLEMENTED_BY]-> Technology
Project -[:DEMONSTRATES]-> Skill

The application uses these relationships to perform multi-hop graph traversals and identify projects that demonstrate multiple skills required by a selected career.

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

\## Screenshots

<img width="1919" height="913" alt="Screenshot 2026-08-19 220428" src="https://github.com/user-attachments/assets/57fa2c5d-118b-4c78-afaa-dd8db3f0176f" />
<img width="1917" height="1020" alt="Screenshot 2026-08-19 220409" src="https://github.com/user-attachments/assets/d8a7d4df-c39b-4f07-8d77-1ecdd703a56f" />
<img width="1919" height="917" alt="Screenshot 2026-08-19 220441" src="https://github.com/user-attachments/assets/fa0dca17-9d4e-42a5-8e43-0a1345456866" />
<img width="1919" height="914" alt="Screenshot 2026-08-19 220528" src="https://github.com/user-attachments/assets/e4bc5f94-ad9d-446a-b22d-fc78d41ca270" />
<img width="1919" height="913" alt="Screenshot 2026-08-19 220455" src="https://github.com/user-attachments/assets/dd51c4e2-ce00-4766-b316-70be2a5851bb" />


\## License



This project is intended as a portfolio and learning project.



````





