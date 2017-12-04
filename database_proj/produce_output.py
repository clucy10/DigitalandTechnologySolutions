"""
This module takes a time-range, radius and postcode to find all the crimes within a
radius of that postcode over a time-range. This is outputted in a form of a histogram
in the console.

ATTRIBUTES:
    time_range (int): inputted by user. This is the number of months passed into the
        month_list function. For example, if this is set to 1, it will return the
        last month. If 6, the last 6 months.
    
    postcode (str): inputted for user to be passed through the centre_point function
        that returns the lat, long for the postcode. This is used to calculate crimes
        within a mile of this geoposition.
    
    radius (int): inputted by user. This is the radius of which the crimes will be
        returned. By requirements, it supposed to return crimes within 1, 2, or
        5 miles. << validation??
    
    date (str): inputted by user. Used in old version to specify which month returns
        the crime data. Not yet included this functionality.
   
    MONTHS (list): uses the time_range variable to return a nested list of the all the
        crime data for the number of months specified.
    
    POSTDATA (tuple): longitude and latitude for the postcode inputted. Used in the
        crimes_in_radius to find the crimes within the radius of the geoposition.
    
    CR_LIST (list): a nested list [[row], [row], [row]] of all the crimes within the
        radius of the postcode geoposition. This is passed to the plot_map function.
        
TO DO:
    Validate the time_range.
    Include the date and postcode validation after testing.
    Allow users to pick a time range or specify the months for the list. This would be
        done in the month_list function.
"""
from compile_csvs import write_csv, month_list
from postcode import centre_point
from crimes_in_box import crimes_in_radius
from plot_map import plot_map

# these are hardcoded for testing purposes. These should be user inputs
time_range = 3
postcode = "EX4 4QJ"
radius = 1
date = "03" # not used in this vers

MONTHS = month_list(time_range) # gets list of months for file names
write_csv(MONTHS) # compile all the crimes into one file

post_data = centre_point(postcode, 'postcodes.csv')

POST_LAT = post_data[0]
POST_LON = post_data[1]

CR_LIST = crimes_in_radius(POST_LAT, POST_LON, radius)

plot_map(CR_LIST, postcode)