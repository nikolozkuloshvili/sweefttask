from flask import Blueprint, request, jsonify
from database import db
from models.author import Author, author_schema, authors_schema
from marshmallow import fields, Schema

author_routes = Blueprint('author_routes', __name__)

# Create a new author
@author_routes.route('/authors', methods=['POST'])
def create_author():
    try:
        name = request.json['name']

        new_author = Author(name=name)

        db.session.add(new_author)
        db.session.commit()

        return jsonify(message='Author created successfully'), 201

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get all authors
@author_routes.route('/authors', methods=['GET'])
def get_authors():
    try:
        authors = Author.query.all()
        result = authors_schema.dump(authors)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get a specific author by ID
@author_routes.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    try:
        author = Author.query.get(author_id)
        if not author:
            return jsonify(message='Author not found'), 404

        result = author_schema.dump(author)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Update an author by ID
@author_routes.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    try:
        name = request.json['name']

        author = Author.query.get(author_id)
        if not author:
            return jsonify(message='Author not found'), 404

        author.name = name

        db.session.commit()

        return jsonify(message='Author updated successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Delete an author by ID
@author_routes.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    try:
        author = Author.query.get(author_id)
        if not author:
            return jsonify(message='Author not found'), 404

        db.session.delete(author)
        db.session.commit()

        return jsonify(message='Author deleted successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
