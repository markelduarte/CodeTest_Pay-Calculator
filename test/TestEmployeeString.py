import datetime
import pytest
import sys

sys.path.insert(0, './../')

from StringParser import EmployeeString
from HoursParser import parseHours
from DeltaCalculator import countHours

class TestEmployeeString:
    
    @pytest.mark.parametrize("x,y", 
    [
        ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 215),
        ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 85),
        ('MARIA=MO10:00-12:00,TH12:00-18:00,SU20:00-21:00', 145),
        ('TOBY=MO10:00-20:00', 160),
        ('ROSE=WE10:00-12:40', 40),
        ('TOM=TH12:00-00:00,SU20:00-21:00', 235)
        ])
    def test_calculatePay(self, x, y):

        employeeString = EmployeeString(x)

        assert employeeString.calculatePay() == y