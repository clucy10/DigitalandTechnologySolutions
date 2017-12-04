# validate date
def validateDate(date):

    """ Checks a string to determine if it is a valid date. Returns a boolean value,
    where True indicates the date is valid, and the date which was tested.
    
    A string 'date' is taken as an argument for this function. If a single digit is
    used to represent the month, this will be modified to the format MM (01,02,03, etc.)
    in the returned date. The date string should only contain numbers, spaces or hyphen
    characters. If the string contains any other character it is invalid, and will not
    be modified.
    
    Returns a boolean value, where True indicates the date is valid, and
    the date which was tested. """
    

    # List of month numbers
    monthsInYear = ["01","02","03","04","05","06","07",
                    "08","09","10","11","12"]
    
    # Remove spaces in string if necessary
    if " " in date:
        date = date.replace(" ", "")
        
    # Remove hyphens in string if necessary
    if "-" in date:
        date = date.replace("-", "")

    if not date.isnumeric():
        # If the date is not numeric, then it is not valid
        valid = False

    else:
    
        if (len(date) == 5) or (len(date) == 6):
            month = date[4:]
            if len(month) == 1:
                # If the user has only used a single digit to specify the month (e.g. '1' for Jan instead of '01') - add a '0' character to the front of the month string
                month = "0" + month
                # Modify the date string so that the month is in the same format as the strings in the array (01, 02, 03, etc)
                date = date[:4] + "0" + date[4:]

            if month in monthsInYear:
                # check to see if the month string is in the array of months (if it is, the month is valid)
                valid = True
            else:
                valid = False
                
        else:
            valid = False
            
    return valid, date
    
    
    
def test_valid():

    validFormat = ["2016-01", "201602", "2012 04", "20161", "20165", "202012"]
    invalidFormat = ["1234", "201614", "2016/01", "2016.01", "20160", "2016012"]
    
    for i in range(len(validFormat)):
        validate, date = validateDate(validFormat[i])
        # If the function caused the date to be modified, print both the original and modified dates
        if validFormat[i] != date:
            print("Original date:", validFormat[i],
                  "\nModified date:", date)
            print("Valid?:", validate)
        else:
            print("Date:", validFormat[i], "\nValid?:", validate)
        print()
        
        
    for j in range(len(invalidFormat)):
        validate, date = validateDate(invalidFormat[j])
        # If the function caused the date to be modified, print both the original and modified dates
        if invalidFormat[j] != date:
            print("Original date:", invalidFormat[j], "\nModified date:", date)
            print("Valid?", validate)
        else:
            print("Date:", invalidFormat[j], "\nValid?", validate)
        print()
        
