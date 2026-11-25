from cmath import atan

from simulation.body_parts import Claws, Teeth
from simulation.combat import PowerCalculator, SimultaneousRound
from simulation.creature import Creature


def _create_test_creature(
        role: str,
        health: int,
        attack_power: int,
        claws: Claws | None = None,
        teeth: Teeth | None = None
) -> Creature:
    return Creature(
        role=role,
        position=0,
        health=health,
        stamina=50,
        attack_power=attack_power,
        num_legs=2,
        num_wings=0,
        claws=claws,
        teeth=teeth
    )


def test_power_calculator_applies_claws_then_teeth() -> None:
    creature = _create_test_creature(
        "Predator",
        health=100,
        attack_power=10,
        claws=Claws.SMALL,
        teeth=Teeth.MEDIUM
    )

    assert PowerCalculator().calculate(creature) == 26


def test_power_calculator_without_modifiers() -> None:
    creature = _create_test_creature(
        "Prey",
        health=100,
        attack_power=10
    )
    assert PowerCalculator().calculate(creature) == 10


def test_simultaneous_round_applies_damage_to_both() -> None:
    predator = _create_test_creature("Predator", health=100, attack_power=10, claws=Claws.SMALL)
    prey = _create_test_creature("Prey", health=60, attack_power=5, teeth=Teeth.MEDIUM)
    round_resolver = SimultaneousRound(PowerCalculator())
    round_resolver.resolve(predator, prey)

    assert predator.health == 89
    assert prey.health == 40