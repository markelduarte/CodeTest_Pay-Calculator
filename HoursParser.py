from datetime import datetime
import re

from HourlyRate import hourlyRateBusinessDays, hourlyRateWeekend

businessDays = ['MO', 'TU', 'WE', 'TH', 'FR']
weekendDays = ['SA', 'SU'] 


# Function for splitting hours into blocks to account for the rate variations 
def parseHours(hoursString):

    # Get day from string
    day = re.search(r'[A-Z][A-Z]',hoursString)
    if day != None:
        day = day.group()
    else:
        return False

    # Get hours from string
    hours = re.search(r'[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]',hoursString)
    if hours != None:
        hours = hours.group()
    else:
        return False

    hoursArray = hours.split('-')

    # Convert time check-in and check-out from string into datetime object
    checkIn = datetime.strptime(hoursArray[0], "%H:%M")
    checkOut = datetime.strptime(hoursArray[1], "%H:%M")

    # If check-out was at midnight, increment date by 1 day in the check-out datetime object
    if checkOut <= checkIn:
        if hoursArray[1] == '00:00':
            checkOut = datetime.strptime('1900-01-02 '+hoursArray[1], "%Y-%m-%d %H:%M")

        else:
            return False


    splitHours = []
    start = checkIn

    # Split datetime objects into blocks that account for the variations in rate
    for key in hourlyRateBusinessDays.keys():
        
        if day in businessDays:
            rate = hourlyRateBusinessDays.get(key)

        elif day in weekendDays:
            rate = hourlyRateWeekend.get(key)

        else:
            return False

        h = []
        lowerBound = datetime.strptime(key[0], "%H:%M")
        upperBound = datetime.strptime('1900-01-01 '+key[1], "%Y-%m-%d %H:%M")

        if key[1] == '00:00':
            upperBound = datetime.strptime('1900-01-02 '+key[1], "%Y-%m-%d %H:%M")

        if start == None:
            start = lowerBound

        if start >= lowerBound and start < upperBound:
            h.append(start)
            
            if checkOut <= upperBound:
                h.append(checkOut)
                splitHours.append((h, rate))
                break

            else:
                h.append(upperBound)

            splitHours.append((h, rate))
            start = None

    # Returns an array of arrays, each internal array has datetime tuple with the time block and its rate
    return splitHours


    

# print(parseHours('MO10:00-12:00'))
# print()
# print(parseHours('TU18:00-00:00'))
# print()
# print(parseHours('WE18:00-18:30'))
# print()
# print(parseHours('TH08:00-18:30'))
# print()
# print(parseHours('FR00:00-00:00'))
# print()
# print(parseHours('SA08:00-00:00'))
# print()
# print(parseHours('SU08:00-00:30')) #False

