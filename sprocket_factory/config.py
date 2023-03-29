"""
Configuration for the Flask app
"""
# pylint: disable=too-few-public-methods

class Config:
    """
    Configuration for the Flask app
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sprocket.db'
