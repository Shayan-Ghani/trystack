from trystack.config import Config
from trystack.trystack import db 
from trystack.util import now, uuidgen

class Project(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    name = db.Column(db.String(256), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=now)
    last_updated_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer, nullable=False, default=Config.DEFAULT_PROJECT_STATUS)