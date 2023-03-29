"""
Routes and views for the sprocketFactory application.
"""
from flask import Blueprint, jsonify, request

from .models import Sprocket, Production
from .models import db

bp = Blueprint("factories", __name__, url_prefix="/sprocketFactory/v1")

# Endpoint to return all sprocket factory data
@bp.route('/production', methods=['GET'])
def get_all_production():
    """
    Return all production data

    Args:
        None

    Returns:
        json: A list of dictionaries containing the production data
    """
    # Get all the production data and group by factory id
    production = Production.query.all()
    return jsonify([{"sprocket_production_actual":p.sprocket_production_actual,
                    "sprocket_production_goal":p.sprocket_production_goal,
                    "time":p.time.isoformat(),
                    "factory_id":p.factory_id} for p in production])

# Endpoint to return factory data for a given factory id
@bp.route('/production/<int:factory_id>', methods=['GET'])
def get_production(factory_id):
    """
    Return production data for a given factory id

    Args:
        factory_id (int): The id of the factory

    Returns:
        json: A list of dictionaries containing the production data for the given factory id
    """
    production = Production.query.filter_by(factory_id=factory_id).all()
    if not production:
        return jsonify({'error': f'No production found for factory_id={factory_id}'}), 404
    return jsonify([{"sprocket_production_actual":p.sprocket_production_actual,
                    "sprocket_production_goal":p.sprocket_production_goal,
                    "time":p.time.isoformat(),
                    "factory_id":p.factory_id} for p in production])

# Endpoint to return all sprockets
@bp.route('/sprockets', methods=['GET'])
def get_all_sprocket():
    """
    Return all sprockets

    Args:
        None

    Returns:
        json: A list of dictionaries containing the sprocket data
    """
    sprocket = Sprocket.query.all()
    return jsonify([{
        'id': sprocket.id,
        'teeth': sprocket.teeth,
        'pitch_diameter': sprocket.pitch_diameter,
        'outside_diameter': sprocket.outside_diameter,
        'pitch': sprocket.pitch
    } for sprocket in sprocket])

# Endpoint to return sprockets for a given id
@bp.route('/sprockets/<int:sprocket_id>', methods=['GET'])
def get_sprocket(sprocket_id):
    """
    Return sprocket for a given id

    Args:
        sprocket_id (int): The id of the sprocket

    Returns:
        json: A dictionary containing the sprocket data for the given id
    """
    sprocket = Sprocket.query.filter_by(id=sprocket_id).first()
    if not sprocket:
        return jsonify({'error': f'No sprocket found for id={sprocket_id}'}), 404
    return jsonify({
        'id': sprocket.id,
        'teeth': sprocket.teeth,
        'pitch_diameter': sprocket.pitch_diameter,
        'outside_diameter': sprocket.outside_diameter,
        'pitch': sprocket.pitch
    })

# Endpoint to create new sprocket
@bp.route('/sprockets', methods=['POST'])
def create_sprocket():
    """
    Create a new sprocket

    Args:
        None 
        - The sprocket data is passed in the request body

    Returns:
        json: A dictionary containing the sprocket data for the newly created sprocket
    """
    data = request.get_json()
    sprocket = Sprocket(
        teeth=data['teeth'],
        pitch_diameter=data['pitch_diameter'],
        outside_diameter=data['outside_diameter'],
        pitch=data['pitch']
    )
    db.session.add(sprocket)
    db.session.commit()
    return jsonify({
        'id': sprocket.id,
        'teeth': sprocket.teeth,
        'pitch_diameter': sprocket.pitch_diameter,
        'outside_diameter': sprocket.outside_diameter,
        'pitch': sprocket.pitch
    })

# Endpoint to update sprocket for a given id
@bp.route('/sprockets/<int:sprocket_id>', methods=['PUT'])
def update_sprocket(sprocket_id):
    """
    Update sprocket for a given id

    Args:
        sprocket_id (int): The id of the sprocket
        - The sprocket data is passed in the request body

    Returns:
        json: A dictionary containing the sprocket data for the given id
    """
    sprocket = Sprocket.query.filter_by(id=sprocket_id).first()
    data = request.get_json()
    sprocket.teeth = data['teeth']
    sprocket.pitch_diameter = data['pitch_diameter']
    sprocket.outside_diameter = data['outside_diameter']
    sprocket.pitch = data['pitch']
    db.session.commit()
    return jsonify({
        'id': sprocket.id,
        'teeth': sprocket.teeth,
        'pitch_diameter': sprocket.pitch_diameter,
        'outside_diameter': sprocket.outside_diameter,
        'pitch': sprocket.pitch
    })
