'''
Created on 20 Nov 2017

This module checks whether the postcode is in the file and
returns the lat, long for the centrepoint as a tuple.

@author: lucy.craddock
'''
import csv

def centre_point(postcode, file):
    file = open(file, 'r')
    postcodes = csv.reader(file)
    postcodes = list(postcodes)  # turns into list to use indices
    firstcol = 0
    for row in postcodes:
        if row[firstcol] == postcode:
            lat = row[10]
            lon = row[11]
            return(float(lat), float(lon))
    file.close()
    raise ValueError # when postcode isn't found
