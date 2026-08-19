from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes.graph import router as graph_router
from app.services.graph_services import DatabaseUnavailableError


app = FastAPI(
    title="CareerGraph API",
    description="Explore career roles, skills, technologies, and projects using a graph database.",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

app.include_router(graph_router)


@app.exception_handler(DatabaseUnavailableError)
async def database_unavailable_handler(
    request: Request,
    exc: DatabaseUnavailableError,
):
    return JSONResponse(
        status_code=503,
        content={
            "detail": str(exc),
            "message": "Please try again later.",
        },
    )


@app.get("/")
def root():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }