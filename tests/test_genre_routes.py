import unittest
from database import app, db  # Import your Flask app and database
from models.genre import Genre  # Import the Genre model
import json

class GenreRoutesTest(unittest.TestCase):
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

    def test_create_genre(self):
        """Test the create genre route"""
        response = self.app.post('/genres', json={
            'name': 'Test Genre'
        })

        self.assertEqual(response.status_code, 201)
        genre = Genre.query.first()
        self.assertIsNotNone(genre)
        self.assertEqual(genre.name, 'Test Genre')

    def test_get_genres(self):
        """Test the get genres route"""
        # Create some test genres
        genre1 = Genre(name='Genre 1')
        genre2 = Genre(name='Genre 2')
        db.session.add_all([genre1, genre2])
        db.session.commit()

        response = self.app.get('/genres')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_genre(self):
        """Test the get genre by ID route"""
        # Create a test genre
        genre = Genre(name='Test Genre')
        db.session.add(genre)
        db.session.commit()

        response = self.app.get(f'/genres/{genre.id}')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Test Genre')

    def test_update_genre(self):
        """Test the update genre by ID route"""
        # Create a test genre
        genre = Genre(name='Test Genre')
        db.session.add(genre)
        db.session.commit()

        response = self.app.put(f'/genres/{genre.id}', json={
            'name': 'Updated Genre Name'
        })

        updated_genre = Genre.query.get(genre.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_genre.name, 'Updated Genre Name')

    def test_delete_genre(self):
        """Test the delete genre by ID route"""
        # Create a test genre
        genre = Genre(name='Test Genre')
        db.session.add(genre)
        db.session.commit()

        response = self.app.delete(f'/genres/{genre.id}')
        deleted_genre = Genre.query.get(genre.id)

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(deleted_genre)

if __name__ == '__main__':
    unittest.main()
