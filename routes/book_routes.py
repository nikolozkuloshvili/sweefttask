from flask import Blueprint, request, jsonify
from database import db
from marshmallow import fields, Schema
from models.book import Book, book_schema, books_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

book_routes = Blueprint('book_routes', __name__)

# Create a new book
@book_routes.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    try:
        title = request.json['title']
        author_id = request.json['author_id']
        genre_id = request.json['genre_id']
        condition_id = request.json['condition_id']

        # Get the current user ID from the JWT token
        current_user_id = get_jwt_identity()

        # Create a new book
        new_book = Book(
            title=title,
            author_id=author_id,
            genre_id=genre_id,
            condition_id=condition_id,
            owner_id=current_user_id  # Set the owner to the current user
        )

        db.session.add(new_book)
        db.session.commit()

        return jsonify(message='Book created successfully'), 201

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get all books
@book_routes.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        result = books_schema.dump(books)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get a specific book by ID
@book_routes.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return jsonify(message='Book not found'), 404

        result = book_schema.dump(book)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Update a book by ID
@book_routes.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    try:
        title = request.json['title']
        author_id = request.json['author_id']
        genre_id = request.json['genre_id']
        condition_id = request.json['condition_id']

        # Get the current user ID from the JWT token
        current_user_id = get_jwt_identity()

        book = Book.query.get(book_id)
        if not book:
            return jsonify(message='Book not found'), 404

        # Check if the current user is the owner of the book
        if current_user_id != book.owner_id:
            return jsonify(message='You do not have permission to update this book'), 403

        # Update the book
        book.title = title
        book.author_id = author_id
        book.genre_id = genre_id
        book.condition_id = condition_id

        db.session.commit()

        return jsonify(message='Book updated successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Delete a book by ID
@book_routes.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    try:
        # Get the current user ID from the JWT token
        current_user_id = get_jwt_identity()

        book = Book.query.get(book_id)
        if not book:
            return jsonify(message='Book not found'), 404

        # Check if the current user is the owner of the book
        if current_user_id != book.owner_id:
            return jsonify(message='You do not have permission to delete this book'), 403

        db.session.delete(book)
        db.session.commit()

        return jsonify(message='Book deleted successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
