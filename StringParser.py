#RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

from DeltaCalculator import countHours
from HoursParser import parseHours


# Class for parsing and storing the data in the input string, and for calculating the amount to pay
class EmployeeString:
    def __init__(self, inputString):

        # Index of the character separating the name from the days and hours
        nameDelimiter = inputString.find('=')

        # Stores name of the employee
        self.name = inputString[:nameDelimiter]

        # Stores an array with each distinct portion of the string containing days and hours worked
        self.hours = inputString[nameDelimiter + 1:].split(',')

        #self.pay = 0

    # Return a dictionary with the name and hours attributes as key and value
    def parseString(self):
        return {self.name: self.hours}

    # Calculates the amount to be paid from the input string
    def calculatePay(self):
        pay = 0

        parsedString = self.parseString()

        # Iterates through each day of the input string
        for s in parsedString[self.name]:
            
            parsedHours = parseHours(s)
            deltaArray = countHours(parsedHours)

            # Gets the total amount to pay by adding the amounts for each day
            for delta in deltaArray:
                pay += delta['Hours'] * delta['Rate'] + delta['Minutes']/60 * delta['Rate']

        #self.pay = pay

        # Returns amount to be paid
        return pay




# x = EmployeeString('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
# print(x.calculatePay())

# x = EmployeeString('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')
# print(x.calculatePay())