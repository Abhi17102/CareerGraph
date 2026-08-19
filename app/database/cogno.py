from neo4j import GraphDatabase

from app.config import settings

driver = GraphDatabase.driver(
    settings.COGNODB_URI,
    auth=(
        settings.COGNODB_USERNAME,
        settings.COGNODB_PASSWORD,
    ),
)