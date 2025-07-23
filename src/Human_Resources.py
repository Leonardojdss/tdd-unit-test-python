from datetime import date

class EmployeeOfBank:
    def __init__(self, name, birth_date, salary):
        self._name = name
        self._birth_date = birth_date
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        birth_date_parts = self._birth_date.split('/')
        birth_year = birth_date_parts[-1]
        current_year = date.today().year
        return current_year - int(birth_year)

    def calculate_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self):
        return f'Employee({self._name}, {self._birth_date}, {self._salary})'