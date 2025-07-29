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
    
    @property
    def surname(self):
        name_complete = self.name.strip()
        name_parts = name_complete.split(" ")
        return " ".join(name_parts[1:])

    def calculate_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            raise Exception("Your salary not permit to receive bonus, bonus is great than 1000")
        return value
    
    def _is_director(self):
        names_director = ["Leonardo José da Silva", "Maria Clara da Silva", "João Pedro da Silva"]
        return self._salary >= 100000 and self._name in names_director

    @property
    def decrease_salary(self):
        if self._is_director():    
            salary_after = self._salary * 0.9
            print(salary_after)

        return salary_after

    def __str__(self):
        return f'Employee({self._name}, {self._birth_date}, {self._salary})'