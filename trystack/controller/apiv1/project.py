from trystack.util import now
from trystack.trystack import db
from trystack.util import jsonify
from trystack.decorator import json_required
from trystack.model import Project
from trystack.schema.apiv1 import ProjectSchema
from flask import request

class ProjectController:
    @json_required
    def get_projects():
        try:
            projects = Project.query.all()
        # many=True is meant to return the collection
        except Exception as e:
            print(e)
            return jsonify(status=500)
        projects_schema = ProjectSchema(many=True)
        return jsonify(
            {"projects": projects_schema.dump(projects) } #provides the state of jsonify
        )
    @json_required    
    def get_project(project_id):
        try:
            project = Project.query.get(project_id)
        except Exception as e:
           print(e)
           return jsonify(status=500)

        if project is None :
            return jsonify(status=404)

        project_schema = ProjectSchema()    
        return jsonify(
            {"project" : project_schema.dump(project)}
        )

    @json_required   
    def create_project():
        project_schema = ProjectSchema(only=["name"])
        try:
            requested_data = project_schema.load(request.get_json())
        except Exception as e:
            print(e)
            return jsonify(status=400)

        try:
            project = Project.query.filter_by(name=requested_data["name"]).first()
        except Exception as e:
            print(e)
            return jsonify(status=500)
        if project is not None:
            return jsonify(status=409)
        project = Project(name=requested_data["name"])
        db.session.add(project)
        
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(status=500)
        # to show list of updated project
        project_schema = ProjectSchema()
        return jsonify(
            {"project" : project_schema.dump(project)},
            status=201
        )

    @json_required
    def update_project(project_id):
        
        project_schema = ProjectSchema(only=["status"])
        try:   
            requested_data = project_schema.load(request.get_json())
        except Exception as e:
            return jsonify(status=400)
        
        if requested_data["status"] > 1 or requested_data["status"] < 0 :
            return jsonify(status=400)

        try:
            project = Project.query.get(project_id)
        except Exception as e:
            print(e)
            return jsonify(status=500) 

        if project is None:
            return jsonify(status=404)
            #checks the status if equall to previous values won't be updated (additional):
        elif requested_data["status"] == project.status:
            return jsonify(status=400, metadata={"Error": f"the state is already {requested_data['status']} so was not updated."})   
        project.status = requested_data["status"]
        project.last_updated_at = now()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(status=500)     
        project_schema = ProjectSchema()
        return jsonify(
            {"project" : project_schema.dump(project)}
        )

    @json_required
    def delete_project(project_id):
        try:
            project = Project.query.get(project_id)
        except Exception as e:
            print(e)
            return jsonify(status=500)

        if project is None :
            return jsonify(status=404) 
        db.session.delete(project)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(status=500)     
        return jsonify(status=204)