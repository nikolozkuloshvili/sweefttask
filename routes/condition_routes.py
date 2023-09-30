from flask import Blueprint, request, jsonify
from database import db
from marshmallow import fields, Schema

from models.condition import Condition, condition_schema, conditions_schema

condition_routes = Blueprint('condition_routes', __name__)

# Create a new condition
@condition_routes.route('/conditions', methods=['POST'])
def create_condition():
    try:
        name = request.json['name']

        new_condition = Condition(name=name)

        db.session.add(new_condition)
        db.session.commit()

        return jsonify(message='Condition created successfully'), 201

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get all conditions
@condition_routes.route('/conditions', methods=['GET'])
def get_conditions():
    try:
        conditions = Condition.query.all()
        result = conditions_schema.dump(conditions)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Get a specific condition by ID
@condition_routes.route('/conditions/<int:condition_id>', methods=['GET'])
def get_condition(condition_id):
    try:
        condition = Condition.query.get(condition_id)
        if not condition:
            return jsonify(message='Condition not found'), 404

        result = condition_schema.dump(condition)
        return jsonify(result), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Update a condition by ID
@condition_routes.route('/conditions/<int:condition_id>', methods=['PUT'])
def update_condition(condition_id):
    try:
        name = request.json['name']

        condition = Condition.query.get(condition_id)
        if not condition:
            return jsonify(message='Condition not found'), 404

        condition.name = name

        db.session.commit()

        return jsonify(message='Condition updated successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

# Delete a condition by ID
@condition_routes.route('/conditions/<int:condition_id>', methods=['DELETE'])
def delete_condition(condition_id):
    try:
        condition = Condition.query.get(condition_id)
        if not condition:
            return jsonify(message='Condition not found'), 404

        db.session.delete(condition)
        db.session.commit()

        return jsonify(message='Condition deleted successfully'), 200

    except Exception as e:
        return jsonify(error=str(e)), 500
