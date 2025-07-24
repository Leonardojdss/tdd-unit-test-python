import pytest
from src.Human_Resources import EmployeeOfBank

# method Given-When-Then

class TestClass:
    def test_then_age_receive_13_03_2000_he_must_22(self):
        #given 
        name="Funcionario_teste"
        birth_date = "13/03/2000"
        age = 25

        #When
        employee = EmployeeOfBank(name, birth_date, 2000)
        result = employee.age()

        #Then
        assert result == age

    def test_then_surname_receive_leonardo_jose_da_silva_he_must_jose_da_silva(self):
        #given
        birth_date = "13/03/2000"
        surname = "jose da silva"
        name="Leonardo jose da silva"

        #When
        employee = EmployeeOfBank(name, birth_date, 2000)
        result = employee.surname

        #then
        assert result == surname

    def test_then_decrease_salary_receive_100000_he_must_90000(self):
        #given
        name="Leonardo José da Silva"
        salary_actual = 100000
        birth_date = "13/03/2000"
        salary_after = 90000

        #When
        employee = EmployeeOfBank(name, birth_date, salary_actual)
        result = employee.decrease_salary

        #then
        assert result == salary_after