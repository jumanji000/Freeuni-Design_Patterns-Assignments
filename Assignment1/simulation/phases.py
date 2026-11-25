from simulation.combat import RoundResolver
from simulation.creature import Creature
from simulation.movement_strategy_selectors import MovementSelector
from simulation.result import Result


class ChasePhase:
    def __init__(self, selector: MovementSelector) -> None:
        self._selector = selector

    def run(self, predator: Creature, prey: Creature) -> bool:
        while True:
            if not self._step(predator):
                return False
            self._step(prey)
            if predator.position >= prey.position:
                return True

    def _step(self, creature: Creature) -> bool:
        movement = self._selector.choose_movement(creature)
        if movement is None:
            return False
        creature.move(movement)
        return True


class FightPhase:
    def __init__(self, resolver: RoundResolver) -> None:
        self._resolver = resolver

    def run(self, predator: Creature, prey: Creature) -> Result:
        while predator.is_alive and prey.is_alive:
            self._resolver.resolve(predator, prey)
        if prey.is_alive:
            return Result.PREY_ESCAPED
        return Result.FIGHT_HAPPENED
