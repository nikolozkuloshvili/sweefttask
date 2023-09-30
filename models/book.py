from database import db
from marshmallow import fields, Schema

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    condition_id = db.Column(db.Integer, db.ForeignKey('condition.id'), nullable=False)
class BookSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'author_id', 'genre_id', 'condition_id')
        model = Book

book_schema = BookSchema()
books_schema = BookSchema(many=True)