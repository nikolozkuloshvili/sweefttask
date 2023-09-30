from database import db
from marshmallow import fields, Schema

class Condition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # Add more fields as needed

class ConditionSchema(Schema):
    class Meta:
        fields = ('id', 'name')  # Add more fields as needed
        model = Condition

condition_schema = ConditionSchema()
conditions_schema = ConditionSchema(many=True)