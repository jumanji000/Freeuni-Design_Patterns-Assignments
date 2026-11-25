import random
from collections.abc import Sequence
from typing import TypeVar

from simulation.body_parts import Claws, Teeth
from simulation.configuration import SimulationConfiguration
from simulation.creature import Creature

T = TypeVar("T")


class CreatureFactory:
    def __init__(
        self, configuration: SimulationConfiguration, rng: random.Random | None = None
    ) -> None:
        self._configuration = configuration
        self._rng = rng if rng is not None else random.Random()

    def create_predator(self) -> Creature:
        return self._create_creature("Predator", position=0)

    def create_prey(self) -> Creature:
        position = self._rng.randint(0, self._configuration.max_prey_position)
        return self._create_creature("Prey", position=position)

    def _create_creature(self, role: str, position: int) -> Creature:
        configuration = self._configuration
        return Creature(
            role=role,
            position=position,
            health=self._rng.randint(*configuration.health_range),
            stamina=self._rng.randint(*configuration.stamina_range),
            attack_power=self._rng.randint(*configuration.power_range),
            num_legs=self._rng.randint(0, configuration.max_num_legs),
            num_wings=self._rng.randint(0, configuration.max_num_wings),
            claws=self._evolve_part(list(Claws)),
            teeth=self._evolve_part(list(Teeth)),
        )

    def _evolve_part(self, options: Sequence[T]) -> T | None:
        if self._rng.random() < self._configuration.part_evolve_chance:
            return self._rng.choice(options)
        return None
