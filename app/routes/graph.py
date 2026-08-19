from fastapi import APIRouter, HTTPException

from app.services.graph_services import (
    get_roles,
    get_role_skills,
    get_role_technologies,
    get_role_projects,
    get_role_graph,
    DatabaseUnavailableError,
)


router = APIRouter(
    prefix="/api",
    tags=["Career Graph"],
)


@router.get("/roles")
def roles():
    return get_roles()


@router.get("/roles/{role_name}/skills")
def role_skills(role_name: str):
    result = get_role_skills(role_name)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Role not found or has no skills.",
        )

    return result


@router.get("/roles/{role_name}/technologies")
def role_technologies(role_name: str):
    result = get_role_technologies(role_name)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Role not found or has no technologies.",
        )

    return result


@router.get("/roles/{role_name}/projects")
def role_projects(role_name: str):
    result = get_role_projects(role_name)

    return result

@router.get("/roles/{role_name}/graph")
def role_graph(role_name: str):
    try:
        result = get_role_graph(role_name)

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Role not found.",
            )

        return result

    except DatabaseUnavailableError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e),
        )