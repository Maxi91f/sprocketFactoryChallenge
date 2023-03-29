"""
Configuration for the Flask app
"""
# pylint: disable=too-few-public-methods
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration for the Flask app
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
