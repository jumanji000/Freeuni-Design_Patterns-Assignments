import pytest

from simulation.body_parts import Claws, Teeth
from simulation.creature import Creature
from simulation.reporting import (
    ConsoleReporter,
    ResultCounter,
    SimulationListener,
    describe_creature,
    describe_evolved_part,
)
from simulation.result import Result


def _sample_creature(
    role: str = "Predator",
    claws: Claws | None = Claws.MEDIUM,
    teeth: Teeth | None = None,
) -> Creature:
    return Creature(
        role=role,
        position=5,
        health=80,
        stamina=40,
        attack_power=6,
        num_legs=2,
        num_wings=1,
        claws=claws,
        teeth=teeth,
    )


def test_describe_part_and_creature() -> None:
    assert describe_evolved_part(None) == "None"
    assert describe_evolved_part(Teeth.HIGH) == "High Teeth Sharpness"

    summary = describe_creature(_sample_creature())
    assert "[Predator] created at position: 5" in summary
    assert "Claws: Medium Claws" in summary
    assert "Teeth: None" in summary


def test_console_reporter_output(capsys: pytest.CaptureFixture[str]) -> None:
    reporter = ConsoleReporter()
    predator = _sample_creature("Predator")
    prey = _sample_creature("Prey")
    counter = ResultCounter()

    reporter.on_simulation_start(1)
    reporter.on_creatures_evolved(predator, prey)
    reporter.on_simulation_end(Result.FIGHT_HAPPENED)
    counter.on_simulation_end(Result.FIGHT_HAPPENED)
    reporter.print_all_simulation_summary(counter.counts, total=1)

    output = capsys.readouterr().out
    assert "---Running simulation: 1---" in output
    assert "Result: Some R-rated things have happened" in output
    assert "Some R-rated things have happened: 1/1" in output
    assert "Prey ran into infinity: 0/1" in output


def test_base_listener_methods_are_noops() -> None:
    listener = SimulationListener()
    creature = _sample_creature()
    listener.on_simulation_start(1)
    listener.on_creatures_evolved(creature, creature)
    listener.on_simulation_end(Result.PREY_ESCAPED)