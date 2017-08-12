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


class ProductionWorker(Employee):

    def __init__(self, name, number, shift_number, hourly_pay):

        Employee.__init__(self, name, number)

        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    def get_shift_number(self):
        return self.__shift_number
    def get_hourly_pay(self):
        return self.__hourly_pay

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

def main():

    name = input("What is the name of your worker? ")
    number = input("What is the employee number? ")
    shift_number = int(input("Is the shift 1, 2 or 3? "))
    hourly_rate = int(input("What is the hourly pay rate? "))

    worker = ProductionWorker(name, number, shift_number, hourly_rate)

    print(worker.get_name())
    print(worker.get_number())
    print(worker.get_shift_number())
    print(worker.get_hourly_pay())

main()