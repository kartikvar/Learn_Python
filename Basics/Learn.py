class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


calc = Calculator(1, 2)
print(calc.add())