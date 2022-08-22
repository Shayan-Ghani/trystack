from flask_restful import Resource

from trystack.controller.apiv1 import ProjectController

class ProjectResource(Resource):
    def get(self, project_id=None):
        if project_id is None:
            return ProjectController.get_projects()
        else:
            return ProjectController.get_project(project_id)

    def post(self):
        return ProjectController.create_project()

    def patch(self, project_id):
        return ProjectController.update_project(project_id)
        
    def delete(self, project_id):
        return ProjectController.delete_project(project_id)