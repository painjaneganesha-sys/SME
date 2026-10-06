from fastapi import APIRouter
import json, os


health_router = APIRouter(prefix="/health")

version_file_path = os.path.join(os.path.dirname(__file__), 'version.json')

with open(version_file_path) as version_file:
    version_data = json.load(version_file)
    Version = version_data.get("Version", "unknown")
    ApplicationName = version_data.get("ApplicationName", "unknown")
    LastEdited = version_data.get("LastEdited", "unknown")
    EditedBy = version_data.get("EditedBy", "unknown")



@health_router.get("/")
async def health_check():
    """ This endpoint checks the health of the service. """
    return {"Status": "healthy", "Version": Version, "Application Name": ApplicationName, "Last Edited": LastEdited, "Edited By": EditedBy}



