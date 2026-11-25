import random

from simulation.combat import PowerCalculator, SimultaneousRound
from simulation.configuration import SimulationConfiguration
from simulation.creature import Creature
from simulation.engine import Simulation
from simulation.factory import CreatureFactory
from simulation.movement_strategy_selectors import GreedyStrategy
from simulation.phases import ChasePhase, FightPhase
from simulation.reporting import ResultCounter, SimulationListener
from simulation.result import Result


class _RecordingListener(SimulationListener):
    def __init__(self) -> None:
        self.events: list[str] = []

    def on_simulation_start(self, simulation_id: int) -> None:
        self.events.append(f"start:{simulation_id}")

    def on_creatures_evolved(self, predator: Creature, prey: Creature) -> None:
        self.events.append(f"evolved:{predator.role}:{prey.role}")

    def on_simulation_end(self, result: Result) -> None:
        self.events.append(f"end:{result.name}")


def test_simulation_notifies_listeners_and_returns_result() -> None:
    config = SimulationConfiguration(max_prey_position=10)
    factory = CreatureFactory(config, rng=random.Random(7))
    recorder = _RecordingListener()
    counter = ResultCounter()

    sim = Simulation(
        factory=factory,
        chase=ChasePhase(GreedyStrategy()),
        fight=FightPhase(SimultaneousRound(PowerCalculator())),
        listeners=[recorder, counter],
    )

    result = sim.run_simulation(simulation_id=3)

    assert result in Result
    assert recorder.events[0] == "start:3"
    assert recorder.events[1] == "evolved:Predator:Prey"
    assert recorder.events[2] == f"end:{result.name}"
    assert counter.counts[result] == 1


def test_simulation_returns_prey_escaped_when_chase_fails() -> None:
    config = SimulationConfiguration(
        max_prey_position=500,
        stamina_range=(0, 0),
    )
    sim = Simulation(
        factory=CreatureFactory(config, rng=random.Random(1)),
        chase=ChasePhase(GreedyStrategy()),
        fight=FightPhase(SimultaneousRound(PowerCalculator())),
        listeners=[],
    )

    assert sim.run_simulation(1) == Result.PREY_ESCAPED