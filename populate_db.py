"""
Populate the database with test data from a json files
"""
import json
import datetime

from sprocket_factory import create_app
from sprocket_factory.models import db, Factory, Sprocket, Production

app = create_app()

with app.app_context():
    # delete all the data from the db
    db.drop_all()
    db.create_all()

    # get the data from test_data.json
    with open('seed_factory_data.json', encoding="utf-8") as test_data:
        factories_data = json.load(test_data)

    # Create factories and chart data objects
    for factory_data in factories_data['factories']:
        factory_obj = Factory(name=factory_data['factory']['name'])
        db.session.add(factory_obj)

        # Flush the session to get the id of the factory
        db.session.flush()

        chart_data = factory_data['factory']['chart_data']

        # For each combination of sprocket_production_actual, sprocket_production_goal, and time
        # create a Production object and add the row to the db
        for production_actual, production_goal, time in zip(*list(chart_data.values())):
            Production_obj = Production(sprocket_production_actual=production_actual,
                                       sprocket_production_goal=production_goal,
                                       time=datetime.datetime.fromtimestamp(time),
                                       factory_id=factory_obj.id)
            db.session.add(Production_obj)


    # get the data from seed_sprocket_data.json
    with open('seed_sprocket_types.json', encoding="utf-8") as test_data:
        sprocket_data = json.load(test_data)

    sprockets = [Sprocket(
        teeth=sprocket['teeth'],
        pitch_diameter=sprocket['pitch_diameter'],
        outside_diameter=sprocket['outside_diameter'],
        pitch=sprocket['pitch']
    ) for sprocket in sprocket_data['sprockets']]


    # add the sprockets to the db
    for sprocket in sprockets:
        db.session.add(sprocket)


    # commit the changes
    db.session.commit()

    # check that the data was added
    print(f"Factories has now {len(Factory.query.all())} records")
    print(f"Sprockets has now {len(Sprocket.query.all())} records")
    print(f"ChartData has now {len(Production.query.all())} records")

    VERVOSE = True

    if VERVOSE:
        # print all the factories
        for factory in Factory.query.all():
            # print all the data
            print(f"Factory: {factory.name}")
            # get all the chart data for the factory
            production = Production.query.filter_by(factory_id=factory.id).all()
            for data in production:
                print(f"Chart data: {data.sprocket_production_actual}, \
{data.sprocket_production_goal}, {data.time}")

        # print all the sprockets
        for sprocket in Sprocket.query.all():
            print(f"Sprocket: {sprocket.teeth}, {sprocket.pitch_diameter}, \
{sprocket.outside_diameter}, {sprocket.pitch}")
