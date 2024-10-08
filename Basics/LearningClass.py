class Calculator:
    num = 10

    def add_numbers(self, a, b):
        return a + b


calc = Calculator()
print("Num is --> {}".format(calc.num))
print("Sum is --> {}".format(calc.add_numbers(2, 3)))