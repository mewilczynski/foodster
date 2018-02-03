# -*- coding: utf-8 -*-

#To install the dependencies, run: pip install -r requirements.txt.

from __future__ import print_function

#import argparse
import json
import pprint
import requests
import sys
import urllib

# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

API_KEY= "fHkSjyMHjIBjR0v0_xxT_PhRH4Nw0wvB_pNvsH7vf-G_leB592KX5UILWyIiyx8Wtbso89oYqVBJSiDasZGtr5aWE5Sdt6GGPgveSMQtSoPiH_vbxAmbQVnNXtJ1WnYx"
API_HOST = 'https://api.yelp.com'

SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
SEARCH_LIMIT = 10

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, categories, term, location, open_now):
    """Query the Search API by a search categories and location.

    Args:
        categories (str): The search categories passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'categories': categories.replace(' ', '+'),
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        #'open_now': open_now.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(categories, term, location, open_now):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, categories, term, location, open_now)

    #response.get returns an array of possible businesses
    businesses = response.get('businesses')

    if not businesses:
        print('No businesses for {0} in {1} found.'.format(term, location))
        return

    name = businesses[0]['name']
    name1 = businesses[1]['name']
    name2 = businesses[2]['name']

    price = businesses[0]["price"]
    price1 = businesses[1]["price"]
    price2 = businesses[2]["price"]

    location = businesses[0]["location"]
    location1 = businesses[1]["location"]
    location2 = businesses[2]["location"]

    print('{0} businesses found, querying business info ' \
        'for the top three results: "{1}", "{2}", and "{3}" ...'.format(
            len(businesses), name, name1, name2))

    # print('Results for business "{0}" found:'.format(name))
    # pprint.pprint(businesses[0]["price"], indent=1)
    # pprint.pprint(businesses[1]["price"], indent=1)
    print('"{0}" \n "{1}" \n "{2}" \n' .format(name, price, location))
    print('"{0}" \n "{1}" \n "{2}" \n' .format(name1, price1, location1))
    print('"{0}" \n "{1}" \n "{2}" \n' .format(name2, price2, location2))


def main():

    categories = "food"
    term = "bread, sandwich, bun"
    location = "Saint Petersburg, FL"
    open_now = True

    try:
        print(term)
        query_api(categories, term, location, open_now)

    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()
