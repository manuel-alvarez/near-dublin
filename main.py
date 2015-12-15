import json
import urllib2


def read_cities(url=""):
    """
    This method reads cities from a given url and stores them in a dictionary of cities when each one of them will have
    a key and another dictionary with its data.
    :param url: string. URL that have a json formatted list of cities
    :return: dictionary. A hash with the cities and their data. If there's any error, this method returns None, and an
    empty dict if list is empty.
    """
    if url == "":
        print "URL Shouln't be emtpy string"
        return None

    try:
        response = urllib2.urlopen(url)
    except (urllib2.HTTPError, ValueError) as e:  # Bad url
        print "Error while reading url: %s" % e.message
        return None

    raw_data = response.read()
    try:
        data = json.loads(raw_data)
    except ValueError as e:
        print "Source file is not well formatted: %s" % e.message
        return None

    return data

def distance(start, end):
    """
    Calculates de distance between two points and returns the number of kilometers between them.
    Points should have be dicts with, at lease, these two attributes:
    - lat: A number representing Latitude
    - lon: A number representing Longitude
    :param start: dict. A dict with both latitude and longitude
    :param end: dict. A dict with both latitude and longitude
    :return: number. The number of kilometers between the two given points. If there's any error, this method returns
    None.
    """
    return 0.0
