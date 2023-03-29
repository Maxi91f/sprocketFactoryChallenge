# pylint: disable=all
from flask import Flask
import pytest
import datetime
import json

from sprocket_factory.routes import bp as factory_bp
from sprocket_factory.models import Factory, Production, Sprocket, db

sample_factory = {"name":'test factory'}
sample_production = {"sprocket_production_actual":100, "sprocket_production_goal":200, "time":datetime.datetime(2020, 1, 1, 0, 0)}
sample_sprocket = {"teeth":10, "pitch_diameter":1.0, "outside_diameter":2.0, "pitch":3.0}

@pytest.fixture(scope='module')
def app():
    """
    Create a Flask app for testing.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(factory_bp)
    
    db.init_app(app)

    return app

@pytest.fixture(scope='module')
def client(app):
    """
    Create a Flask test client for testing.
    """
    return app.test_client()

@pytest.fixture(scope='module')
def init_database(app):
    """
    Initiate a database for testing.
    """
    with app.app_context():
        # Add simple data to the database
        db.create_all()

        factory = Factory(**sample_factory)
        db.session.add(factory)
        db.session.flush()

        production = Production(**sample_production, factory_id=factory.id)
        db.session.add(production)

        sprocket = Sprocket(**sample_sprocket)
        db.session.add(sprocket)
        
        db.session.commit()
    yield db
    with app.app_context():
        db.drop_all()

def test_production(client, init_database):
    """
    Test the production table.
    """
    production = client.get('/sprocketFactory/v1/production')
    print(production.data)
    response = json.loads(production.data)[0]
    assert response["sprocket_production_actual"] == sample_production["sprocket_production_actual"]
    assert response["sprocket_production_goal"] == sample_production["sprocket_production_goal"]
    assert response["time"] == sample_production["time"].isoformat()
    assert response["factory_id"] == 1

def test_production_id(client, init_database):
    """
    Test the production table with id.
    """
    production = client.get('/sprocketFactory/v1/production/1')
    response = json.loads(production.data)[0]
    assert response["sprocket_production_actual"] == sample_production["sprocket_production_actual"]
    assert response["sprocket_production_goal"] == sample_production["sprocket_production_goal"]
    assert response["time"] == sample_production["time"].isoformat()
    assert response["factory_id"] == 1

def test_sprocket(client, init_database):
    """
    Test the sprocket table.
    """
    sprocket = client.get('/sprocketFactory/v1/sprockets')
    response = json.loads(sprocket.data)[0]
    assert response["teeth"] == sample_sprocket["teeth"]
    assert response["pitch_diameter"] == sample_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == sample_sprocket["outside_diameter"]
    assert response["pitch"] == sample_sprocket["pitch"]

def test_sprocket_id(client, init_database):
    """
    Test the sprocket table with id.
    """
    sprocket = client.get('/sprocketFactory/v1/sprockets/1')
    response = json.loads(sprocket.data)
    assert response["teeth"] == sample_sprocket["teeth"]
    assert response["pitch_diameter"] == sample_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == sample_sprocket["outside_diameter"]
    assert response["pitch"] == sample_sprocket["pitch"]

def test_sprocket_post(client, init_database):
    """
    Test the sprocket table with post.
    """
    second_sprocket = {"teeth":20, "pitch_diameter":2.0, "outside_diameter":2.0, "pitch":3.0}
    sprocket = client.post('/sprocketFactory/v1/sprockets', json=second_sprocket)
    response = json.loads(sprocket.data)
    assert response["teeth"] == second_sprocket["teeth"]
    assert response["pitch_diameter"] == second_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == second_sprocket["outside_diameter"]
    assert response["pitch"] == second_sprocket["pitch"]

    # Test that the sprocket was added to the database
    sprocket = client.get('/sprocketFactory/v1/sprockets/2')
    response = json.loads(sprocket.data)
    assert response["teeth"] == second_sprocket["teeth"]
    assert response["pitch_diameter"] == second_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == second_sprocket["outside_diameter"]
    assert response["pitch"] == second_sprocket["pitch"]

def test_sprocket_put(client, init_database):
    """
    Test the sprocket table with put.
    """
    second_sprocket = {"teeth":40, "pitch_diameter":2.0, "outside_diameter":2.0, "pitch":3.0}
    sprocket = client.put('/sprocketFactory/v1/sprockets/2', json=second_sprocket)
    response = json.loads(sprocket.data)
    assert response["teeth"] == second_sprocket["teeth"]
    assert response["pitch_diameter"] == second_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == second_sprocket["outside_diameter"]
    assert response["pitch"] == second_sprocket["pitch"]

    # Test that the sprocket was modified in the database
    sprocket = client.get('/sprocketFactory/v1/sprockets/2')
    response = json.loads(sprocket.data)
    assert response["teeth"] == second_sprocket["teeth"]
    assert response["pitch_diameter"] == second_sprocket["pitch_diameter"]
    assert response["outside_diameter"] == second_sprocket["outside_diameter"]
    assert response["pitch"] == second_sprocket["pitch"]


