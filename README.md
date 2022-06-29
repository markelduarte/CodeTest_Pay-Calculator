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

- The HourlyRate module, which has a dictionary containing the different blocks of time throughout the day and their respective rates.


| Input                                                                             | Output                             |
| ----------------------------------------------------------------------------------| ---------------------------------- |
| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00        | The amount to pay RENE is: 215 USD |
| ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00                                  | The amount to pay ASTRID is: 85 USD|
