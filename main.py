import concurrent.futures
from StringParser import EmployeeString
import sys

filename = sys.argv[1]

# Wraps the process of calculating amount to be paid in one function
def executionWrapper(line):
    try:
        employee = EmployeeString(line.strip())
        pay = employee.calculatePay()
        pay = '{:.0f}'.format(pay) if float(pay).is_integer() else '{:.2f}'.format(pay)
        return f'The amount to pay {employee.name} is: {pay} USD'

    # Catches the error if the input is not a valid string
    except:
        return 'The string is not valid.'


def main():

    # Reads input txt file
    with open(filename, 'r') as f:
        content = f.readlines()

        # Launches parallel tasks for processing the input strings
        with concurrent.futures.ProcessPoolExecutor() as executor:

            # Calculates the amount to be paid for each line in the input file
            results = executor.map(executionWrapper, content)

            # Prints the amount to be paid for each line in the input file
            for result in results:
                print(result)


if __name__ == "__main__":
    main()