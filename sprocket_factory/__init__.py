"""
The main application module for sprocketFactory.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .routes import bp as factory_bp
from .models import db

def create_app():
    """
    Create the Flask app and register the blueprints.

    Args:
        None
    
    Returns:
        app (Flask): The Flask app
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(factory_bp)
    return app
