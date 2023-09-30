from database import db
from marshmallow import fields, Schema

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # Add more fields as needed

class GenreSchema(Schema):
    class Meta:
        fields = ('id', 'name')  # Add more fields as needed
        model = Genre

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)