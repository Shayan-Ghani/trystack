from trystack.trystack import ma 
from trystack.model import Project

class ProjectSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Project
    
    id = ma.auto_field(dump_only=True)
    name = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
    last_updated_at = ma.auto_field(dump_only=True)
    status = ma.auto_field()