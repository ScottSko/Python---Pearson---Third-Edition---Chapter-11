class Person:

    def __init__(self, name, address, phone_number):

        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def phone_number(self):
        return self.__phone_number

class Customer(Person):

    def __init__(self, name, address, phone_number, customer_number):

        Person.__init__(self, name, address, phone_number)
        self.__customer_number = customer_number
        self.__mailing_list = False

    def get_customer_number(self):
        return self.__customer_number
    def get_mailing_list(self):
        return self.__mailing_list

    def set_mailing_list(self):
        self.__mailing_list = True

def main():

    name = "Scott"
    address = "443 Webber Court"
    phone_number = "703-945-3400"
    customer_number = 5

    customer = Customer(name, address, phone_number, customer_number)

    print(customer.get_mailing_list())

    print("Does", customer.get_name(), "want to be on a mailing list? ", end='')
    desire = input("y/n? ")

    if desire.lower() == "y":
        customer.set_mailing_list()
        print(customer.get_name(), "is now on the mailing list.")
    else:
        print(customer.get_name(), "is not on the mailing list.")

    print(customer.get_mailing_list())

main()