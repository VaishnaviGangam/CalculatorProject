# calculator/calculation.py
from .calculator import Calculator

class Calculation:
    def __init__(self, operator: str, operand_a: float, operand_b: float):
        self.operator = operator
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.result = self.perform_operation()

    def perform_operation(self) -> float:
        if self.operator == 'add':
            return Calculator.add(self.operand_a, self.operand_b)
        elif self.operator == 'subtract':
            return Calculator.subtract(self.operand_a, self.operand_b)
        elif self.operator == 'multiply':
            return Calculator.multiply(self.operand_a, self.operand_b)
        elif self.operator == 'divide':
            return Calculator.divide(self.operand_a, self.operand_b)
        else:
            raise ValueError(f"Unknown operation {self.operator}")
