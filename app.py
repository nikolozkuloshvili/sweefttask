from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from config import Config  # Import your Config class from config.py
from flask_migrate import Migrate
from config import Config
from database import db, init_db  # Import the SQLAlchemy instance and init_db function from database.py
app = Flask(__name__)

app.config.from_object(Config)  # Assuming you have a configuration setup
init_db(app)

ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Import and register blueprints for routes
from routes.user_routes import user_routes
from routes.book_routes import book_routes
from routes.author_routes import author_routes
from routes.genre_routes import genre_routes
from routes.condition_routes import condition_routes

# Register the blueprints
app.register_blueprint(user_routes)
app.register_blueprint(book_routes)
app.register_blueprint(author_routes)
app.register_blueprint(genre_routes)
app.register_blueprint(condition_routes)

if __name__ == '__main__':
    app.run(debug=True)
