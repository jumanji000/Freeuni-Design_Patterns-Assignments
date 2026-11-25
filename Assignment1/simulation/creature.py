from collections.abc import Sequence
from dataclasses import dataclass

from simulation.body_parts import Claws, PowerModifier, Teeth
from simulation.movement import MovementStrategy


@dataclass
class Creature:
    role: str
    position: int
    health: int
    stamina: int
    attack_power: int
    num_legs: int
    num_wings: int
    claws: Claws | None = None
    teeth: Teeth | None = None

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def power_modifiers(self) -> Sequence[PowerModifier]:
        modifiers: list[PowerModifier] = []
        if self.claws is not None:
            modifiers.append(self.claws)
        if self.teeth is not None:
            modifiers.append(self.teeth)
        return modifiers

    def move(self, strategy: MovementStrategy) -> None:
        self.stamina = max(0, self.stamina - strategy.stamina_cost)
        self.position += strategy.distance

    def take_damage(self, damage: int) -> None:
        self.health -= damage
