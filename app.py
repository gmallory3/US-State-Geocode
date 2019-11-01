import logging
import requests
from datetime import datetime
from database.tables import db
from resources.constants import OUTPUT_FORMAT, GOOGLE_GEOCODE_BASE_URL, API_KEY
from resources.util import create_geocoding_params, parse_geocode_response
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

STARTUP_TIME = datetime.now()

app = Flask(__name__)

file_handler = logging.FileHandler(f'logs/api_log_{STARTUP_TIME.date()}_{STARTUP_TIME.timestamp()}.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


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
        'key': API_KEY
    }

    geocoding_params = create_geocoding_params(param_dict)
    geocoding_api_url = f'{GOOGLE_GEOCODE_BASE_URL}{OUTPUT_FORMAT}?{geocoding_params}'

    if request.method == 'GET':
        response = requests.get(geocoding_api_url)
        return jsonify(parse_geocode_response(response))


if __name__ == '__main__':
    app.debug = True
    app.logger.info(f'Server start time: {STARTUP_TIME}')

    db.create_all()

    app.run(host='0.0.0.0', port=4996)
