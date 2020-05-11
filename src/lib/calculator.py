# coding=utf-8
from decimal import *
import utils

class Calculator:
    # a, op, b must be strings
    def __init__(self, a, op, b):
        self.res = 0.0
        self.valid = False
        self.number1 = 0.0
        self.number2 = 0.0
        self.operator = ""
        a = a.replace(',', '')
        b = b.replace(',', '')
        if self.validate_digits(a) and self.validate_digits(b):
            self.res, self.operator = self.calculate(a, b, op)
            self.valid = True
            self.number1 = a
            self.number2 = b
        else:
            raise SyntaxError("Invalid Input. Check Input File")

    def calculate(self, a, b, op, digits=12):
        # switch of operations
        if op == '+':
            return self.addition(a, b, digits), '+'
        elif op == '-' or op == '−':
            return self.subtraction(a, b, digits), '-'
        elif op == 'x' or op == '*' or op == '×':
            return self.multiplication(a, b, digits), 'x'
        elif op == '/' or op == '÷':
            return self.division(a, b, digits), '/'
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
                raise SyntaxError("Too many decimal digits")
            if len(array[0]) <= 15 and len(array[1]) <= 15 - len(array[0]):
                return True
            else:
                raise SyntaxError("Too many digits")
        elif len(array) == 1:
            if len(array[0]) <= 15:
                return True
        else:
            raise SyntaxError("Too many input arguments. (Check the input file)")

    def validate_numbers(self, a, b):
        a = float(a)
        b = float(b)
        # if b < 0:
        #     raise ValueError("Second Input must be Positive")
        if not type(a) is float:
            raise TypeError("Invalid First Input")
        if not type(b) is float:
            raise TypeError("Invalid Second Input")
        return True

    def division(self, a, b, dig):
        if self.validate_numbers(a, b):
            b = float(b)
            if b == 0.0:
                raise ZeroDivisionError("Invalid Zero Division")
            getcontext().prec = dig
            return Decimal(a) /  Decimal(b)

    def addition(self, a, b, dig):
        if self.validate_numbers(a, b):
            getcontext().prec = dig
            return Decimal(a) + Decimal(b)

    def subtraction(self, a, b, dig):
        if self.validate_numbers(a, b):
            b = float(b)
            if b < 0.0:
                b = b*-1

            getcontext().prec = dig
            return Decimal(a) - Decimal(b)

    def multiplication(self, a, b, dig):
        if self.validate_numbers(a, b):
            getcontext().prec = dig
            return Decimal(a) * Decimal(b)

    def validate_result(self, result):
        # edge case
        if str(self.res) == "-0":
            self.res = 0
        result = result.encode('ascii', 'replace')
        result = result.replace('?', '-')
        result = result.replace(',', '')
        result = Decimal(result)
        return utils.isclose(float(result), float(self.res))
