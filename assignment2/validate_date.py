# validate date


def validateDate(date):

    """ Checks a string to determine if it is a valid date. Returns a boolean value,
    where True indicates the date is valid, and the date which was tested.
    
    A string 'date' is taken as an argument for this function. If a single digit is
    used to represent the month, this will be modified to the format MM (01,02,03, etc.)
    in the returned date. The date string should only contian numbers, spaces or hyphen
    characters. If the string contains any other character it is invalid, and will not
    be modified.
    
    Returns a boolean value, where True indicates the date is valid, and
    the date which was tested. If the date is valid, it is returned in the format 'YYYY-MM'.
    If invalid, it is returned in its original state. """
    

    # List of month numbers
    monthsInYear = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    
    # Remove spaces in string if necessary
    if " " in date:
        date = date.replace(" ", "")
        
    # Remove hyphens in string if necessary
    if "-" in date:
        date = date.replace("-", "")

    # Test that this string now only contains numbers
    if not date.isnumeric():
        # If the date is not numeric, then it is not valid
        valid = False

    else:
    
        if (len(date) == 5) or (len(date) == 6):
            month = date[4:]
            if len(month) == 1:
                # If the user has only used a single digit to specify the month (e.g. '1' for Jan instead of '01') - add a '0' character to the front of the month string
                month = "0" + month

            if month in monthsInYear:
                # check to see if the month string is in the array of months (if it is, the month is valid)
                valid = True
                # Modify the date string so that it is in the format 'YYYY-MM'
                date = date = date[:4] + "-" + month
                
            else:
                valid = False
                
        else:
            valid = False
            
    return valid, date
      
    
if __name__ == "__main__":
    # Main method not executed on import
    
    # Valid format dates
    assert validate_date("2016-01") == True, "2016-01"
    assert validate_date("201602") == True, "2016-02"
    assert validate_date("2012 04") == True, "2012-04"
    assert validate_date("20161") == True, "2016-01"
    assert validate_date("20165") == True, "2016-05"
    assert validate_date("202012") == True, "2020-12"
    
    # Invalid format dates
    assert validate_date("1234") == False, "1234"
    assert validate_date("201614") == False, "201614"
    assert validate_date("2016/01") == False, "2016/01"
    assert validate_date("2016.01") == False, "2016.01"
    assert validate_date("20160") == False, "20160"
    assert validate_date("2016012") == False, "2016012"
    
    print("All tests run successfully!")
    
