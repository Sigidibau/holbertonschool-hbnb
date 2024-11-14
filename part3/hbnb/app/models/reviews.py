from hbnb.app.models.basemodel import BaseModel
from hbnb.app.models.places import Place
from hbnb.app.models.users import User
from hbnb.app import db, bcrypt

class Review(BaseModel):
    tablename__ = 'reviews'

first_name = db.Column(db.String(50), nullable=False)
last_name = db.Column(db.String(50), nullable=False)
email = db.Column(db.String(120), nullable=False, unique=True)
password = db.Column(db.String(128), nullable=False)
is_admin = db.Column(db.Boolean, default=False)



def validations(self):
    # Rating validation, must be between 0 and 5
    if self.rating < 0 or self.rating > 5:
        raise ValueError("Rating must be between 0 and 5")

    # Review text can't be empty
    if self.text is None:
        raise ValueError("Review required")

    # Validate place and user ids to ensure they are properly assigned
    if not isinstance(self.place_id, str) or not self.place_id:
        raise ValueError("Place ID must be valid.")

    if not isinstance(self.user_id, str) or not self.user_id:
        raise ValueError("User ID must be valid.")