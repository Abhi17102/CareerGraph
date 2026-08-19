from app.services.graph_services import (
    get_roles,
    get_role_skills,
    get_role_technologies,
    get_role_projects,
)


print("\n=== ROLES ===")
print(get_roles())

print("\n=== SKILLS ===")
print(get_role_skills("Python Backend Developer"))

print("\n=== TECHNOLOGIES ===")
print(get_role_technologies("Python Backend Developer"))

print("\n=== PROJECTS ===")
print(get_role_projects("Python Backend Developer"))