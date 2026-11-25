from enum import Enum
from typing import Protocol


class PowerModifier(Protocol):
    def modify_power(self, power: int) -> int: ...


class Claws(Enum):
    SMALL = (2, "Small Claws")
    MEDIUM = (3, "Medium Claws")
    LARGE = (4, "Large Claws")

    def __init__(self, damage_multiplier: int, description: str) -> None:
        self.damage_multiplier = damage_multiplier
        self.description = description

    def modify_power(self, power: int) -> int:
        return power * self.damage_multiplier


class Teeth(Enum):
    LOW = (3, "Low Teeth Sharpness")
    MEDIUM = (6, "Medium Teeth Sharpness")
    HIGH = (9, "High Teeth Sharpness")

    def __init__(self, damage_boost: int, description: str) -> None:
        self.damage_boost = damage_boost
        self.description = description

    def modify_power(self, power: int) -> int:
        return power + self.damage_boost
