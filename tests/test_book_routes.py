import unittest
from database import app, db  # Import your Flask app and database
from models.author import Author  # Import the Author model
from models.genre import Genre  # Import the Genre model
from models.condition import Condition  # Import the Condition model
from models.book import Book  # Import the Book model
import json

class BookRoutesTest(unittest.TestCase):
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

    def test_create_book(self):
        """Test the create book route"""
        # Create a test author, genre, and condition
        author = Author(name='Test Author')
        genre = Genre(name='Test Genre')
        condition = Condition(name='Test Condition')
        db.session.add_all([author, genre, condition])
        db.session.commit()

        response = self.app.post('/books', json={
            'title': 'Test Book',
            'author_id': author.id,
            'genre_id': genre.id,
            'condition_id': condition.id
        })

        self.assertEqual(response.status_code, 201)
        book = Book.query.first()
        self.assertIsNotNone(book)
        self.assertEqual(book.title, 'Test Book')

    def test_get_books(self):
        """Test the get books route"""
        # Create some test authors, genres, and conditions
        author1 = Author(name='Author 1')
        author2 = Author(name='Author 2')
        genre1 = Genre(name='Genre 1')
        genre2 = Genre(name='Genre 2')
        condition1 = Condition(name='Condition 1')
        condition2 = Condition(name='Condition 2')
        db.session.add_all([author1, author2, genre1, genre2, condition1, condition2])
        db.session.commit()

        # Create some test books
        book1 = Book(title='Book 1', author_id=author1.id, genre_id=genre1.id, condition_id=condition1.id)
        book2 = Book(title='Book 2', author_id=author2.id, genre_id=genre2.id, condition_id=condition2.id)
        db.session.add_all([book1, book2])
        db.session.commit()

        response = self.app.get('/books')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_book(self):
        """Test the get book by ID route"""
        # Create a test author, genre, condition, and book
        author = Author(name='Test Author')
        genre = Genre(name='Test Genre')
        condition = Condition(name='Test Condition')
        db.session.add_all([author, genre, condition])
        db.session.commit()
        book = Book(title='Test Book', author_id=author.id, genre_id=genre.id, condition_id=condition.id)
        db.session.add(book)
        db.session.commit()

        response = self.app.get(f'/books/{book.id}')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Test Book')

    def test_update_book(self):
        """Test the update book by ID route"""
        # Create a test author, genre, condition, and book
        author = Author(name='Test Author')
        genre = Genre(name='Test Genre')
        condition = Condition(name='Test Condition')
        db.session.add_all([author, genre, condition])
        db.session.commit()
        book = Book(title='Test Book', author_id=author.id, genre_id=genre.id, condition_id=condition.id)
        db.session.add(book)
        db.session.commit()

        response = self.app.put(f'/books/{book.id}', json={
            'title': 'Updated Book Title'
        })

        updated_book = Book.query.get(book.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_book.title, 'Updated Book Title')

    def test_delete_book(self):
        """Test the delete book by ID route"""
        # Create a test author, genre, condition, and book
        author = Author(name='Test Author')
        genre = Genre(name='Test Genre')
        condition = Condition(name='Test Condition')
        db.session.add_all([author, genre, condition])
        db.session.commit()
        book = Book(title='Test Book', author_id=author.id, genre_id=genre.id, condition_id=condition.id)
        db.session.add(book)
        db.session.commit()

        response = self.app.delete(f'/books/{book.id}')
        deleted_book = Book.query.get(book.id)

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(deleted_book)

if __name__ == '__main__':
    unittest.main()
