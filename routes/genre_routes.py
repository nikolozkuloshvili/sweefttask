from flask import Blueprint, request, jsonify
from database import db
from models.genre import Genre, genre_schema, genres_schema
from marshmallow import fields, Schema

genre_routes = Blueprint('genre_routes', __name__)

# Create a new genre
@genre_routes.route('/genres', methods=['POST'])
def create_genre():
    try:
        name = request.json['name']

        new_genre = Genre(name=name)

        db.session.add(new_genre)
        db.session.commit()

        return jsonify(message='Genre created successfully'), 201

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get all genres
@genre_routes.route('/genres', methods=['GET'])
def get_genres():
    try:
        genres = Genre.query.all()
        result = genres_schema.dump(genres)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get a specific genre by ID
@genre_routes.route('/genres/<int:genre_id>', methods=['GET'])
def get_genre(genre_id):
    try:
        genre = Genre.query.get(genre_id)
        if not genre:
            return jsonify(message='Genre not found'), 404

        result = genre_schema.dump(genre)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Update a genre by ID
@genre_routes.route('/genres/<int:genre_id>', methods=['PUT'])
def update_genre(genre_id):
    try:
        name = request.json['name']

        genre = Genre.query.get(genre_id)
        if not genre:
            return jsonify(message='Genre not found'), 404

        genre.name = name

        db.session.commit()

        return jsonify(message='Genre updated successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Delete a genre by ID
@genre_routes.route('/genres/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    try:
        genre = Genre.query.get(genre_id)
        if not genre:
            return jsonify(message='Genre not found'), 404

        db.session.delete(genre)
        db.session.commit()

        return jsonify(message='Genre deleted successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
