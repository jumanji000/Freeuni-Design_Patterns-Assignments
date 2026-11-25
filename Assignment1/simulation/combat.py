from typing import Protocol

from simulation.creature import Creature


class PowerCalculator:
    def calculate(self, creature: Creature) -> int:
        power = creature.attack_power
        for modifier in creature.power_modifiers():
            power = modifier.modify_power(power)
        return power


class RoundResolver(Protocol):
    def resolve(self, predator: Creature, prey: Creature) -> None: ...


class SimultaneousRound:
    def __init__(self, calculator: PowerCalculator) -> None:
        self._calculator = calculator

    def resolve(self, predator: Creature, prey: Creature) -> None:
        predator_damage = self._calculator.calculate(predator)
        prey_damage = self._calculator.calculate(prey)
        prey.take_damage(predator_damage)
        predator.take_damage(prey_damage)
