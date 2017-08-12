class Employee:

    def __init__(self, name, number):

        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number

    def __str__(self):

        return self.__name + self.__number

class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, yearly_bonus):

        Employee.__init__(self, name, number)

        self.__salary = salary
        self.__yearly_bonus = yearly_bonus

    def get_salary(self):
        return self.__salary
    def get_yearly_bonus(self):
        return self.__yearly_bonus

def main():

    name = "Scott"
    number = "12345"
    salary = 100000
    yearly_bonus = 5000

    supervisor = ShiftSupervisor(name, number, salary, yearly_bonus)

    print("The supervisor's name is", supervisor.get_name())
    print("The supervisor's number is", supervisor.get_number())
    print("The supervisor's salary is", "$" + format(supervisor.get_salary(), ",.0f"))
    print("The supervisor's yearly bonus is", supervisor.get_yearly_bonus())

main()