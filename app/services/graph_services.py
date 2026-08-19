from neo4j import exceptions

from app.database.cogno import driver


class DatabaseUnavailableError(Exception):
    pass


def get_roles():
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (r:Role)
                RETURN r.name AS name, r.description AS description
                ORDER BY r.name
                """
            )

            return [record.data() for record in result]

    except exceptions.Neo4jError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the graph database."
        ) from e


def get_role_skills(role_name: str):
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (r:Role {name: $role_name})-[:REQUIRES]->(s:Skill)
                RETURN s.name AS name, s.category AS category
                ORDER BY s.name
                """,
                role_name=role_name,
            )

            return [record.data() for record in result]

    except exceptions.Neo4jError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the graph database."
        ) from e


def get_role_technologies(role_name: str):
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (r:Role {name: $role_name})
                      -[:REQUIRES]->(s:Skill)
                      -[:IMPLEMENTED_BY]->(t:Technology)
                RETURN DISTINCT
                       t.name AS name,
                       t.type AS type
                ORDER BY t.name
                """,
                role_name=role_name,
            )

            return [record.data() for record in result]

    except exceptions.Neo4jError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the graph database."
        ) from e


def get_role_projects(role_name: str):
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (r:Role {name: $role_name})-[:REQUIRES]->(s:Skill)
                      <-[:DEMONSTRATES]-(p:Project)

                WITH p, collect(DISTINCT s.name) AS matching_skills

                WHERE size(matching_skills) >= 3

                RETURN
                       p.name AS name,
                       p.description AS description,
                       matching_skills,
                       size(matching_skills) AS match_count

                ORDER BY match_count DESC, p.name
                """,
                role_name=role_name,
            )

            return [record.data() for record in result]

    except exceptions.Neo4jError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the graph database."
        ) from e

def get_role_graph(role_name: str):
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (r:Role {name: $role_name})

                OPTIONAL MATCH (r)-[:REQUIRES]->(s:Skill)

                WITH r, collect(DISTINCT s) AS skills

                OPTIONAL MATCH (skill:Skill)-[:IMPLEMENTED_BY]->(t:Technology)
                WHERE skill IN skills

                WITH
                    r,
                    skills,
                    collect(DISTINCT {
                        name: t.name,
                        type: t.type,
                        skill: skill.name
                    }) AS technologies

                OPTIONAL MATCH (p:Project)-[:DEMONSTRATES]->(project_skill:Skill)
                WHERE project_skill IN skills

                WITH
                    r,
                    skills,
                    technologies,
                    p,
                    collect(DISTINCT project_skill.name) AS matching_skills

                WITH
                    r,
                    skills,
                    technologies,
                    collect(
                        DISTINCT CASE
                            WHEN p IS NOT NULL
                            AND size(matching_skills) >= 3
                            THEN {
                                name: p.name,
                                description: p.description,
                                matching_skills: matching_skills
                            }
                        END
                    ) AS projects

                RETURN
                    r.name AS role,

                    [
                        x IN skills |
                        {
                            id: "skill-" + x.name,
                            label: x.name,
                            type: "skill"
                        }
                    ] AS skill_nodes,

                    technologies,

                    projects
                """,
                role_name=role_name,
            )

            record = result.single()

            if not record:
                return None

            data = record.data()

            nodes = [
                {
                    "id": "role",
                    "label": data["role"],
                    "type": "role",
                }
            ]

            edges = []

            # Skills
            for skill in data["skill_nodes"]:
                nodes.append(skill)

                edges.append({
                    "data": {
                        "source": "role",
                        "target": skill["id"],
                        "label": "REQUIRES",
                    }
                })

            # Technologies
            for technology in data["technologies"]:
                if not technology["name"]:
                    continue

                technology_node = {
                    "id": f"technology-{technology['name']}",
                    "label": technology["name"],
                    "type": "technology",
                }

                nodes.append(technology_node)

                skill_name = technology["skill"]

                if skill_name:
                    skill_id = f"skill-{skill_name}"

                    if any(node["id"] == skill_id for node in nodes):
                        edges.append({
                            "data": {
                                "source": skill_id,
                                "target": technology_node["id"],
                                "label": "IMPLEMENTED_BY",
                            }
                        })

            # Projects
            for project in data["projects"]:
                if not project:
                    continue

                project_node = {
                    "id": f"project-{project['name']}",
                    "label": project["name"],
                    "type": "project",
                    "description": project["description"],
                    "matching_skills": project["matching_skills"],
                }

                nodes.append(project_node)

                for skill_name in project["matching_skills"]:
                    skill_id = f"skill-{skill_name}"

                    if any(node["id"] == skill_id for node in nodes):
                        edges.append({
                            "data": {
                                "source": skill_id,
                                "target": project_node["id"],
                                "label": "DEMONSTRATES",
                            }
                        })

            return {
                "nodes": nodes,
                "edges": edges,
            }

    except exceptions.Neo4jError as e:
        raise DatabaseUnavailableError(
            "Unable to connect to the graph database."
        ) from e