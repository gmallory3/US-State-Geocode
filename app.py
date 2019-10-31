from datetime import datetime
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from resources import resources
from resources.util import create_geocoding_params, parse_geocode_response
import requests

STARTUP_TIME = datetime.now()

app = Flask(__name__)

file_handler = logging.FileHandler(f'logs/api_log_{STARTUP_TIME.date()}_{STARTUP_TIME.timestamp()}.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

OUTPUT_FORMAT = 'json'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
# db = SQLAlchemy(app)
#
# ' vs '

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Book
#
# # Connect to Database and create database session
# engine = create_engine('sqlite:///books-collection.db?check_same_thread=False')
# Base.metadata.bind = engine
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# Geocoding API info: https://developers.google.com/maps/documentation/geocoding/intro
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY


@app.route('/', methods=['GET'])
def home():
    """
    API endpoint returning light example of reference documentation.
    :return: String html
    """

    app.logger.info('Load Homepage')
    return '''
        <h1> US State Geolocator API </h1>
        <p> 
            Please enter an address to receive the latitude, longitude, and state name. 
        </p>
        <p>
            Other functionality includes:
                ...
        </p>'''


@app.route('/api/v1/find_state/<string:address>', methods=['GET'])
def get_state_from_address(address):
    """
    API endpoint example
    :return: JSON of example dictionary
    """
    param_dict = {
        'address': address,
        'key': resources.API_KEY
    }

    geocoding_params = create_geocoding_params(param_dict)
    geocoding_api_url = f'{resources.GOOGLE_GEOCODE_BASE_URL}{OUTPUT_FORMAT}?{geocoding_params}'

    if request.method == 'GET':
        response = requests.get(geocoding_api_url)
        return jsonify(parse_geocode_response(response))


if __name__ == '__main__':
    app.debug = True
    app.logger.info(f'Server start time: {STARTUP_TIME}')
    app.run(host='0.0.0.0', port=4996)

#     status definitions on https://developers.google.com/maps/documentation/geocoding/intro

#  todo: include the shape files I used to confirm it's the same as what Sang is expecting
#  todo: investigate packaging DB with submission
#  todo: docker this stuff. "it works on my machine" isn't a valid excuse
#  todo: Street View Publish API could give image of the address as API endpoint
#  todo: swagger
#  todo: define tests in postman sandbox
