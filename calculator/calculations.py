# calculator/calculations.py
from typing import List, Optional
from .calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def last_calculation(cls) -> Optional[Calculation]:
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history.copy()

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()
