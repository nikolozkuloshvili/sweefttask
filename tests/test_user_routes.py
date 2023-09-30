import unittest
from database import app, db  # Import your Flask app and database
from models.user import Users  # Import the User model

class UserRoutesTest(unittest.TestCase):
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

    def test_register_user(self):
        """Test the user registration route"""
        response = self.app.post('/register', json={
            'email': 'test@example.com',
            'password': 'test_password'
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Users.query.count(), 1)  # Check if a user was added to the database

    def test_login_user(self):
        """Test the user login route"""
        # Register a user first
        self.app.post('/register', json={
            'email': 'test@example.com',
            'password': 'test_password'
        })

        response = self.app.post('/login', json={
            'email': 'test@example.com',
            'password': 'test_password'
        })

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
