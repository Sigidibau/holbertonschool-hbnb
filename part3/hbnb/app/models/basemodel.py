from datetime import datetime
from  hbnb.app import db
import uuid

class BaseModel:
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

    def to_dict(self):
        """Convert the object attributes to a dictionary for serialization"""
        result = self.__dict__.copy()
        # Convert datetime fields to ISO format
        if 'created_at' in result:
            result['created_at'] = result['created_at'].isoformat()
        if 'updated_at' in result:
            result['updated_at'] = result['updated_at'].isoformat()
        return result