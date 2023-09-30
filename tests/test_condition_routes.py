import unittest
from database import app, db  # Import your Flask app and database
from models.condition import Condition  # Import the Condition model
import json

class ConditionRoutesTest(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'  # Use an in-memory SQLite database for testing
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Tear down the test environment"""
        db.session.remove()
        db.drop_all()

    def test_create_condition(self):
        """Test the create condition route"""
        response = self.app.post('/conditions', json={
            'name': 'Test Condition'
        })

        self.assertEqual(response.status_code, 201)
        condition = Condition.query.first()
        self.assertIsNotNone(condition)
        self.assertEqual(condition.name, 'Test Condition')

    def test_get_conditions(self):
        """Test the get conditions route"""
        # Create some test conditions
        condition1 = Condition(name='Condition 1')
        condition2 = Condition(name='Condition 2')
        db.session.add_all([condition1, condition2])
        db.session.commit()

        response = self.app.get('/conditions')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_condition(self):
        """Test the get condition by ID route"""
        # Create a test condition
        condition = Condition(name='Test Condition')
        db.session.add(condition)
        db.session.commit()

        response = self.app.get(f'/conditions/{condition.id}')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Test Condition')

    def test_update_condition(self):
        """Test the update condition by ID route"""
        # Create a test condition
        condition = Condition(name='Test Condition')
        db.session.add(condition)
        db.session.commit()

        response = self.app.put(f'/conditions/{condition.id}', json={
            'name': 'Updated Condition Name'
        })

        updated_condition = Condition.query.get(condition.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_condition.name, 'Updated Condition Name')

    def test_delete_condition(self):
        """Test the delete condition by ID route"""
        # Create a test condition
        condition = Condition(name='Test Condition')
        db.session.add(condition)
        db.session.commit()

        response = self.app.delete(f'/conditions/{condition.id}')
        deleted_condition = Condition.query.get(condition.id)

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(deleted_condition)

if __name__ == '__main__':
    unittest.main()
