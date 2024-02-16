"""This module provides Calculator class with basic arithmetic operations."""


# calculator/calculator.py
class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Adds two numbers together.
        
        :param a: float - first number to add
        :param b: float - second number to add
        :return: float - the sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Subtracts the second number from the first.
        
        :param a: float - number to be subtracted from
        :param b: float - number to subtract
        :return: float - the difference of a and b
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiplies two numbers together.
        
        :param a: float - first number to multiply
        :param b: float - second number to multiply
        :return: float - the product of a and b
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides the first number by the second.
        
        :param a: float - number to be divided
        :param b: float - number to divide by
        :return: float - the quotient of a and b
        :raises ZeroDivisionError: if b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
