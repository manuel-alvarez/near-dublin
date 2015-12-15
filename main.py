import json
import math
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
    RADIUS = 6371  # In Kilometers

    if (not isinstance(start, dict)) or (not 'lat' in start.keys()) or (not 'lon' in start.keys()) or \
            (not isinstance(start['lat'], float)) or (not isinstance(start['lon'], float)):
        print "Start point is not properly configured"
        return None
    if (not isinstance(end, dict)) or (not 'lat' in end.keys()) or (not 'lon' in end.keys()) or \
            (not isinstance(end['lat'], float)) or (not isinstance(end['lon'], float)):
        print "End point is not properly configured"
        return None

    # convert degrees to radians
    start_lat = start['lat'] * math.pi / 180
    start_lon = start['lon'] * math.pi / 180
    end_lat = end['lat'] * math.pi / 180
    end_lon = end['lon'] * math.pi / 180

    # delta_lat = abs(start_lat - end_lat)  # Not used in this formula
    delta_lon = abs(start_lon - end_lon)

    central_angle = math.acos((math.sin(start_lat) * math.sin(end_lat)) + (math.cos(start_lat) * math.cos(end_lat) * math.cos(delta_lon)))
    dist = RADIUS * central_angle
    return dist

