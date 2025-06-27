from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from app.utils import setup_logging

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    print("create_app() called successfully")

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    setup_logging()

    # Register existing blueprint
    from app.routes import blueprint
    app.register_blueprint(blueprint, url_prefix='/api')

    # Register new author and book APIs
    from app.Routes.authors_api import authors_api
    from app.Routes.books_api import books_api
    app.register_blueprint(authors_api)
    app.register_blueprint(books_api)

    return app
