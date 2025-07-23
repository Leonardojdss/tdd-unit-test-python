import pytest
from src.Human_Resources import EmployeeOfBank

# method Given-When-Then

class TestClass:
    def test_then_age_receive_13_03_2000_he_must_22(self):
        #given 
        birth_date = "13/03/2000"
        age = 25

        employee = EmployeeOfBank("Funcionario_teste", birth_date, 2000)

        #When
        result = employee.age()

        #Then
        assert result == age
