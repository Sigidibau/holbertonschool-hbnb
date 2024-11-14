#!/usr/bin/python3


from  hbnb.app.models.basemodel import BaseModel
from hbnb.app import db, bcrypt

class Amenity(BaseModel):
    tablename__ = 'Amenity'

first_name = db.Column(db.String(50), nullable=False)
last_name = db.Column(db.String(50), nullable=False)
email = db.Column(db.String(120), nullable=False, unique=True)
password = db.Column(db.String(128), nullable=False)
is_admin = db.Column(db.Boolean, default=False)

    

def amenity_validation(self):
    # Required, maximum length of 50 characters.
    if not self.name or len(self.name) > 50:
        raise ValueError("Amenity name must be less than 50 characters")