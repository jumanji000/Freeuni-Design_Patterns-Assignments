from collections.abc import Callable, Sequence

from simulation.creature import Creature
from simulation.factory import CreatureFactory
from simulation.phases import ChasePhase, FightPhase
from simulation.reporting import SimulationListener
from simulation.result import Result


class Simulation:
    def __init__(
        self,
        factory: CreatureFactory,
        chase: ChasePhase,
        fight: FightPhase,
        listeners: Sequence[SimulationListener],
    ) -> None:
        self._factory = factory
        self._chase = chase
        self._fight = fight
        self._listeners = listeners

    def run_simulation(self, simulation_id: int) -> Result:
        self._notify(lambda listener: listener.on_simulation_start(simulation_id))
        predator = self._factory.create_predator()
        prey = self._factory.create_prey()
        self._notify(lambda listener: listener.on_creatures_evolved(predator, prey))
        result = self._resolve(predator, prey)
        self._notify(lambda listener: listener.on_simulation_end(result))
        return result

    def _resolve(self, predator: Creature, prey: Creature) -> Result:
        if not self._chase.run(predator, prey):
            return Result.PREY_ESCAPED
        return self._fight.run(predator, prey)

    def _notify(self, event: Callable[[SimulationListener], None]) -> None:
        for listener in self._listeners:
            event(listener)
