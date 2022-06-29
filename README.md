# CodeTest_Pay-Calculator

## Running the program (Ubuntu)
Open the Ubuntu terminal in the project directory and run the main.py module followed by a .txt file containing the input strings for the program.

Ex:
```
$ python3 main.py input.txt
```
The input.txt file in this repository contains the input strings for the progam.

The python3 command may differ, depending on the operating system.



## How the code is structured
The program is divided in 5 modules:

- The main module, which starts the program;

- The StringParser module, that contains the class EmployeeString,
which receives an input string and uses the method calculatePay() to get the amount to be paid based on the input string;

- The HoursParser module, which has a function called parseHours that is used get an array of datetime objects from the input string;

- The DeltaCalculator module, which has a function called countHours, which receives the return from the function parseHours and calculates the amount of
hours worked based on the difference between the time when the employee check in and the time when the employee checked out;

- The HourlyRate module, which has a dictionary containing the blocks of time over the course of a day and their respective rates (for business days and weekends).

## How it works

The prorgam is called through the main module which instanciates an EmployeeString object, passing a string read from the .txt file as argument, and calls the method calculatePay. Upon instanciation, the EmployeeString stores the name and the hours extracted from the input string in it's attributes. The method parseString from the EmployeeString object retrieves theses values from the name and hours attributes of the class and returns these values in the form of a dictionary, upon execution.

When the method calculatePay is called, it executes the parseString method and uses the value returned as input for the parseHours function, which, then, returns an array of tuples, each tuple containing a block of time in the datetime format and it's respective hourly rate, obtained from the HourlyRates module. The calculatePay method, then, used the value returned by the parseHours function as input for the countHours function, which returns an array of dictionaries containing the number of hours in each block of time received as input, along with their rates. The calculatePay method takes each element of this array of dictionaries to multiply the number of hours in each block by their respective rates and returns a sum of all these results as the total amount to be paid.

In the end, the main method shows the total amount to be paid in the output string for each line in the input .txt file.
The main module has a function called executionWrapper that instanciates the EmployeeString object and runs the calculatePay method. This wrapper is used as an argument for the concurrent.futures executor in order to process many lines of the input file simultaneously in parallel processes.

### Inputs and Outputs

- executionWrapper (Instanciates EmployeeString object and runs EmployeeString.calculatePay() method)

| Input                                                                             | Output                             |
| ----------------------------------------------------------------------------------| ---------------------------------- |
| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00        | The amount to pay RENE is: 215 USD |
| ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00                                  | The amount to pay ASTRID is: 85 USD|

##
- parseHours

| Input                                                                             | Output                             |
| ----------------------------------------------------------------------------------| ---------------------------------- |
| 'SA08:00-00:00'        | [([datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 9, 0)], 30),([datetime.datetime(1900, 1, 1, 9, 0), datetime.datetime(1900, 1, 1, 18, 0)], 20), ([datetime.datetime(1900, 1, 1, 18, 0), datetime.datetime(1900, 1, 2, 0, 0)], 25)]|

##
- countHours

| Input                                                                             | Output                             |
| ----------------------------------------------------------------------------------| ---------------------------------- |
| [([datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 9, 0)], 30),([datetime.datetime(1900, 1, 1, 9, 0), datetime.datetime(1900, 1, 1, 18, 0)], 20), ([datetime.datetime(1900, 1, 1, 18, 0), datetime.datetime(1900, 1, 2, 0, 0)], 25)]        | [{'Hours': 1, 'Minutes': 0, 'Rate': 30}, {'Hours': 9, 'Minutes': 0, 'Rate': 20},{'Hours': 6, 'Minutes': 0, 'Rate': 25}]|

##

### Tests
The test folder in this repository contains the unit tests for the Employee.calculatePay method (TestEmployeeString.py) and for the parseHours and countHours functions (TestModules.py)

To run these tests it's necessary to have Pytest installed.

#### Installing Pytest
Run in the terminal:
```
$ pip install pytest
```
or run the following command in the root directory of this project:
```
$ pip install -r requirements.txt
```


#### Running Tests
Testing EmployeeString.calculatePay method:

```
$ pytest TestEmployeeString.py
```
Testing parseHours and countHours functions:
```
$ pytest TestModules.py
```
