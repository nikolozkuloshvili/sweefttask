from database import db
from marshmallow import fields, Schema

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # Add more fields as needed
    
class AuthorSchema(Schema):
    class Meta:
        fields = ('id', 'name')  # Add more fields as needed
        model = Author

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)