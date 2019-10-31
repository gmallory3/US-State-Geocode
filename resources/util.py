"""
Utility Functions
"""


def create_geocoding_params(param_dict):
    """
    Turn a dictionary with the address into  Google Geocode API parameter string
    :param param_dict: dictionary with keys address and key
    :return: google_geocode_parameters
    """
    # Note: Country should be specified in address or component filter, but not both.
    #       If country is present in address, remove it
    address_elements = param_dict['address'].split()
    if address_elements[-1].lower() in ['us', 'usa', 'united states', 'united states of america']:
        address_elements.pop()
    address_elements = [element.strip(',') for element in address_elements]

    formatted_address = 'address=' + '+'.join(address_elements)
    country_filter = '&components=country:US'
    api_key = '&key=' + param_dict['key']

    return formatted_address + country_filter + api_key


def reverse_geocode(param_dict):
    """
    Convert a latitude & longitude into a Google Geocode API parameter string
    :param param_dict:
    :return: google_geocode_parameters
    """
    latitude = param_dict['latitude']
    longitude = param_dict['longitude']
    api_key = '&key=' + param_dict['key']

    return f'latlng={latitude},{longitude}' + api_key


def parse_geocode_response(response):
    """
    Parse longitude, latitude, and state from Google Geocode API response object.
    :param response: Google Geocode API response object
    :return: 3-tuple: (latitude, longitude, state)
    """
    status = response.json()['status']
    if status != 'OK':
        return {'status_code': 400,
                'status': 'Bad Request'}

    try:
        # In the case of ambiguity, there will be multiple results. These are generally ordered in specificity
        address = response.json()['results'][0]

        latitude = address['geometry']['location']['lat']
        longitude = address['geometry']['location']['lng']

        state = None
        for component in address['address_components']:

            if component['types'][0] == 'administrative_area_level_1':
                state = component['long_name']

        return {'latitude': latitude,
                'longitude': longitude,
                'state': state
                }

    except (ValueError, KeyError) as error:
        return {'status_code': 400,
                'status': 'Bad Request',
                'error': error}
