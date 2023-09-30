from flask import Blueprint, request, jsonify, current_app
from database import db
from marshmallow import fields, Schema
from flask_bcrypt import Bcrypt  # Import Bcrypt from flask_bcrypt
from models.user import Users, user_schema, users_schema
from flask_jwt_extended import jwt_required, create_access_token

user_routes = Blueprint('user_routes', __name__)

bcrypt = Bcrypt()  # Initialize Bcrypt

@user_routes.route('/register', methods=['POST'])
def register():
    print("Route accessed")
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            print("Email already exists")
            return jsonify(message='Email already exists'), 400

        # Hash the password using bcrypt
        hashed_password = bcrypt.generate_password_hash(password.encode('utf-8'), 12).decode('utf-8')

        new_user = Users(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        print("User registered successfully")

        return jsonify(message='User registered successfully'), 201

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify(error=str(e)), 500

@user_routes.route('/login', methods=['POST'])
def login():
    try:
        email = request.json['email']
        password = request.json['password']

        # Find the user by email
        user = Users.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Generate access token
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Invalid credentials'), 401

    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f'Error during user login: {str(e)}')

        return jsonify(error=str(e)), 500
