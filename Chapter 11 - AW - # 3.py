def main():

    class Beverage:
        def __init__(self, bev_name):
            self.__bev_name = bev_name
        def message(self):
            print("I'm a beverage.")

    class Cola(Beverage):
        def __init__(self):
            Beverage.__init__(self, "cola")
        def message(self):
            print("I'm a cola.")

    b = Beverage("water")
    c = Cola()
    b.message()
    c.message()


main()