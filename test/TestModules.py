import datetime
import pytest
import sys

sys.path.insert(0, './../')

from HoursParser import parseHours
from DeltaCalculator import countHours


def test_parseHours():

    x = 'SA08:00-00:00'
    y = [([datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 9, 0)], 30), 
    ([datetime.datetime(1900, 1, 1, 9, 0), datetime.datetime(1900, 1, 1, 18, 0)], 20), 
    ([datetime.datetime(1900, 1, 1, 18, 0), datetime.datetime(1900, 1, 2, 0, 0)], 25)]

    assert parseHours(x) == y

    x = 'SU08:00-00:30'
    y = False
    
    assert parseHours(x) == y

def test_countHours():
    x = [([datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 9, 0)], 30), 
        ([datetime.datetime(1900, 1, 1, 9, 0), datetime.datetime(1900, 1, 1, 18, 0)], 20), 
        ([datetime.datetime(1900, 1, 1, 18, 0), datetime.datetime(1900, 1, 2, 0, 0)], 25)]

    y = [{'Hours': 1, 'Minutes': 0, 'Rate': 30}, 
    {'Hours': 9, 'Minutes': 0, 'Rate': 20}, 
    {'Hours': 6, 'Minutes': 0, 'Rate': 25}]

    assert countHours(x) == y
