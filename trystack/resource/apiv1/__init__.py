from trystack.trystack import apiv1 as api
from .project import ProjectResource

api.add_resource(
    ProjectResource,
    "/projects",
    methods=["GET", "POST"],
    endpoint="projects"
)

api.add_resource(
    ProjectResource,
    "/projects/<project_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="project"
)