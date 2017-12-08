import math

def bounding_box(latlng, radius):
    """
    src: https://stackoverflow.com/questions/3182260/python-geocode-filtering-by-distance/3183539
    Passes postcode latlong and radius to find the maximum and minimum
    longitude and latitude for the bounding box. The aim of this function is
    to reduce the amount of times the haversine formula code is used as this
    is the heaviest part of the program.
    """
    EARTH_R = 6371.009  # radius from center of the sphere in km
    lat, lng = latlng   # unpacks tuple

    radius = radius * 1.60934 # turns the radius, given in miles, to km

    # some math
    dlat = radius / EARTH_R
    dlon = math.asin(math.sin(dlat) / math.cos(math.radians(lat)))
    dlat = math.degrees(dlat)
    dlon = (math.degrees(dlon))

    lat_min = lat - dlat
    lat_max = lat + dlat

    lon_min = lng -dlon
    lon_max = lng + dlon

    return(lat_min, lat_max, lon_min, lon_max)
