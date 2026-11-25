from collections.abc import Sequence
from typing import Protocol

from simulation.movement import DEFAULT_STRATEGIES, MovementStrategy, Mover


class MovementSelector(Protocol):
    def choose_movement(self, creature: Mover) -> MovementStrategy | None: ...


class GreedyStrategy:
    def __init__(
        self, strategies: Sequence[MovementStrategy] = DEFAULT_STRATEGIES
    ) -> None:
        self._strategies = strategies

    def choose_movement(self, creature: Mover) -> MovementStrategy | None:
        usable = [s for s in self._strategies if s.can_perform(creature)]
        return max(usable, key=lambda s: s.distance, default=None)


class StaminaSaverStrategy:
    def __init__(
        self, strategies: Sequence[MovementStrategy] = DEFAULT_STRATEGIES
    ) -> None:
        self._strategies = strategies

    def choose_movement(self, creature: Mover) -> MovementStrategy | None:
        usable = [s for s in self._strategies if s.can_perform(creature)]
        return min(usable, key=lambda s: (s.stamina_cost, -s.distance), default=None)
