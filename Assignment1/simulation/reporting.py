from collections import Counter
from collections.abc import Mapping

from simulation.body_parts import Claws, Teeth
from simulation.creature import Creature
from simulation.result import Result


class SimulationListener:
    def on_simulation_start(self, simulation_id: int) -> None:
        pass

    def on_creatures_evolved(self, predator: Creature, prey: Creature) -> None:
        pass

    def on_simulation_end(self, result: Result) -> None:
        pass


def describe_evolved_part(part: Claws | Teeth | None) -> str:
    return part.description if part is not None else "None"


def describe_creature(creature: Creature) -> str:
    return (
        f"[{creature.role}] created at position: {creature.position}, "
        f"Health: {creature.health}, "
        f"Stamina: {creature.stamina}, "
        f"Attack power: {creature.attack_power}, "
        f"Number of legs: {creature.num_legs}, "
        f"Number of wings: {creature.num_wings}, "
        f"Claws: {describe_evolved_part(creature.claws)}, "
        f"Teeth: {describe_evolved_part(creature.teeth)}"
    )


class ConsoleReporter(SimulationListener):
    def on_simulation_start(self, simulation_id: int) -> None:
        print(f"\n---Running simulation: {simulation_id}---")

    def on_creatures_evolved(self, predator: Creature, prey: Creature) -> None:
        print(describe_creature(predator))
        print(describe_creature(prey))

    def on_simulation_end(self, result: Result) -> None:
        print(f"Result: {result.value}")

    def print_all_simulation_summary(
        self, counts: Mapping[Result, int], total: int
    ) -> None:
        print("\n---All Simulation Summary---")
        for result in Result:
            print(f"{result.value}: {counts.get(result, 0)}/{total}")


class ResultCounter(SimulationListener):
    def __init__(self) -> None:
        self.counts: Counter[Result] = Counter()

    def on_simulation_end(self, result: Result) -> None:
        self.counts[result] += 1
