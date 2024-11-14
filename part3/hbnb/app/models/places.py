#!/usr/bin/python3
from hbnb.app.models.basemodel import BaseModel
from hbnb.app.models.users import User
from hbnb.app import db, bcrypt
import uuid


class Place(BaseModel):
    tablename__ = 'place'

first_name = db.Column(db.String(50), nullable=False)
last_name = db.Column(db.String(50), nullable=False)
email = db.Column(db.String(120), nullable=False, unique=True)
password = db.Column(db.String(128), nullable=False)
is_admin = db.Column(db.Boolean, default=False)



def validations(self):
    # Validates required length of title
    if not self.title or len(self.title) > 100:
        raise ValueError('Maximum length of 100 characters')

    # Ensures the owner exists
    if not isinstance(self.owner, User):
        raise ValueError('Owner must be a User')

    # Price must be a positive value
    if self.price < 1:
        raise ValueError('Price must be greater than 0')

    # Latitude must be within the range of -90.0 to 90.0.
    if not (-90.0 <= self.latitude <= 90.0):
        raise ValueError('Latitude must be between -90 and 90')
    # Longitude must be within the range of -180.0 to 180.0.
    if not (-180.0 <= self.longitude <= 180.0):
        raise ValueError('Longitude must be between -180 and 180')

def add_review(self, review):
    """Add a review to the place."""
    self.reviews.append(review)

def add_amenity(self, amenity):
    """Add an amenity to the place."""
    self.amenities.append(amenity)