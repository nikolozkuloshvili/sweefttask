from database import db
from marshmallow import fields, Schema

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'email')  # Add more fields as needed
        model = Users

user_schema = UserSchema()
users_schema = UserSchema(many=True)