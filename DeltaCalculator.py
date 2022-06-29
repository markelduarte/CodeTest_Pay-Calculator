# from HoursParser import parseHours
# from datetime import datetime
# import re


# Takes the return from the parseHours function and calculates the number of hours worked
def countHours(hoursArray):

    timeBlocks =[]

    # Iterates through each block of time in the input of the function
    for hours in hoursArray:
        
        # Stores the hourly rate for the function's return
        rate = hours[1]

        # Timedelta object with the number of hours in the block            
        delta = hours[0][1] - hours[0][0]

        # Converts timedelta object to hours
        hoursDelta = delta.seconds//3600

        # Takes the minutes remainder of the timedelta
        minutes = delta.seconds//60 % 60

        # If check-in and check-out time are both 00:00, ascribes the value 24 to the number of hours worked
        if delta.days == 1:
            hoursDelta = 24

        # Appends a list with a dictionary containing the number of hours and minutes worked and its rate
        timeBlocks.append({'Hours': hoursDelta, 'Minutes':minutes, 'Rate': rate})

    return timeBlocks

# print(countHours('MO10:00-12:00'))
# print()
# print(countHours('MO18:00-00:00'))
# print()
# print(countHours('MO18:00-18:30'))
# print()
# print(countHours('MO08:00-18:30'))
# print()
# print(countHours('MO00:00-00:01'))
# print()
# print(countHours('MO00:00-00:00'))
# print()
# print(countHours('MO08:00-00:30')) #False

# print(countHours(parseHours('SA08:00-00:00')))