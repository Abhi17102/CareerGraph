from app.database.cogno import driver


def test_role_skills():
    with driver.session() as session:
        result = session.run(
            """
            MATCH (r:Role {name: $role_name})-[:REQUIRES]->(s:Skill)
            RETURN r.name AS role, s.name AS skill, s.category AS category
            ORDER BY s.name
            """,
            role_name="Python Backend Developer",
        )

        print("\nSkills required:")
        for record in result:
            print(
                f"- {record['skill']} "
                f"({record['category']})"
            )

def test_role_technologies():
    with driver.session() as session:
        result = session.run(
            """
            MATCH (r:Role {name: $role_name})
                  -[:REQUIRES]->(s:Skill)
                  -[:IMPLEMENTED_BY]->(t:Technology)
            RETURN DISTINCT
                   r.name AS role,
                   s.name AS skill,
                   t.name AS technology
            ORDER BY technology
            """,
            role_name="Python Backend Developer",
        )

        print("\nTechnologies connected to role:")
        for record in result:
            print(
                f"- {record['technology']} "
                f"(through {record['skill']})"
            )

def test_projects_for_role():
    with driver.session() as session:
        result = session.run(
            """
            MATCH (r:Role {name: $role_name})-[:REQUIRES]->(s:Skill)
                  <-[:DEMONSTRATES]-(p:Project)
            RETURN DISTINCT
                   p.name AS project,
                   collect(s.name) AS matching_skills
            ORDER BY project
            """,
            role_name="Python Backend Developer",
        )

        print("\nProjects matching role:")
        for record in result:
            print(
                f"- {record['project']}: "
                f"{', '.join(record['matching_skills'])}"
            )

if __name__ == "__main__":
    try:
        test_role_skills()
        test_role_technologies()
        test_projects_for_role()
    finally:
        driver.close()