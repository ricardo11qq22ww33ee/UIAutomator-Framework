

class Calculator:
    # a, op, b must be strings
    def __init__(self, a, op, b):
        self.res = 0.0
        self.valid = False
        self.number1 = 0.0
        self.number2 = 0.0
        self.operator = ""
        if self.validate_digits(a) and self.validate_digits(b):
            self.res = self.calculate(a, b, op)
            self.valid = True
            self.number1 = a
            self.number2 = b
            self.operator = op
        else:
            raise SyntaxError("invalid input")

    def calculate(self, a, b, op):
        # switch of operations
        if op == '+':
            return self.addition(a, b)
        elif op == '-':
            return self.subtraction(a, b)
        elif op == 'x':
            return self.multiplication(a, b)
        elif op == '/':
            return self.division(a, b)
        else:
            raise SyntaxError("Unsupported Operation")

    def validate_digits(self, n):
        # no more than 15 digits total, and max 10 in decimals
        if "." in n:
            array = n.split(".")
        else:
            array = [n]
        if len(array) == 2:
            if len(array[1]) > 10:
                return False
            if len(array[0]) <= 15 and len(array[1]) <= 15 - len(array[0]):
                return True
        elif len(array) == 1:
            if len(array[0]) <= 15:
                return True
        else:
            raise SyntaxError("Too many input arguments. (Check the input file)")

    def validate_numbers(self, a, b):
        a = float(a)
        b = float(b)
        if not type(a) is float:
            raise TypeError("Invalid First Input")
        if not type(b) is float:
            raise TypeError("Invalid Second Input")
        return True

    def division(self, a, b):
        if self.validate_numbers(a, b):
            b = float(b)
            if b == 0.0:
                raise ZeroDivisionError("Invalid Zero Division")
            return float(a) / float(b)

    def addition(self, a, b):
        if self.validate_numbers(a, b):
            return float(a) + float(b)

    def subtraction(self, a, b):
        if self.validate_numbers(a, b):
            return float(a) - float(b)

    def multiplication(self, a, b):
        if self.validate_numbers(a, b):
            return float(a) * float(b)
