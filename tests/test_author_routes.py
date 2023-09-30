import unittest
from database import app, db  # Import your Flask app and database
from models.author import Author  # Import the Author model
import json

class AuthorRoutesTest(unittest.TestCase):
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

    def test_create_author(self):
        """Test the create author route"""
        response = self.app.post('/authors', json={
            'name': 'Test Author'
        })

        self.assertEqual(response.status_code, 201)
        author = Author.query.first()
        self.assertIsNotNone(author)
        self.assertEqual(author.name, 'Test Author')

    def test_get_authors(self):
        """Test the get authors route"""
        # Create some test authors
        author1 = Author(name='Author 1')
        author2 = Author(name='Author 2')
        db.session.add_all([author1, author2])
        db.session.commit()

        response = self.app.get('/authors')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_author(self):
        """Test the get author by ID route"""
        # Create a test author
        author = Author(name='Test Author')
        db.session.add(author)
        db.session.commit()

        response = self.app.get(f'/authors/{author.id}')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Test Author')

    def test_update_author(self):
        """Test the update author by ID route"""
        # Create a test author
        author = Author(name='Test Author')
        db.session.add(author)
        db.session.commit()

        response = self.app.put(f'/authors/{author.id}', json={
            'name': 'Updated Author Name'
        })

        updated_author = Author.query.get(author.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_author.name, 'Updated Author Name')

    def test_delete_author(self):
        """Test the delete author by ID route"""
        # Create a test author
        author = Author(name='Test Author')
        db.session.add(author)
        db.session.commit()

        response = self.app.delete(f'/authors/{author.id}')
        deleted_author = Author.query.get(author.id)

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(deleted_author)

if __name__ == '__main__':
    unittest.main()
