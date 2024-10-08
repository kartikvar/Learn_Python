class Calculator:

    def __init__(self, a, b):
        print("Constructor initiated")
        self.a = a
        self.b = b

    def add_numbers(self):
        return self.a + self.b


calc = Calculator(2, 3)
print("Sum is --> {}".format(calc.add_numbers()))
