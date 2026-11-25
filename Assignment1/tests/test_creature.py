from simulation.body_parts import Claws, Teeth
from simulation.creature import Creature
from simulation.movement import Crawl, Fly


def _create_test_creature(
        *,
        health: int = 100,
        stamina: int = 100,
        attack_power: int = 10,
        num_legs: int = 2,
        num_wings: int = 2,
        claws: Claws | None = None,
        teeth: Teeth | None = None
) -> Creature:
    return Creature(
        role="Predator",
        position=0,
        health=health,
        stamina=stamina,
        attack_power=attack_power,
        num_legs=num_legs,
        num_wings=num_wings,
        claws=claws,
        teeth=teeth
    )


def test_is_alive() -> None:
    assert _create_test_creature(health=1).is_alive is True
    assert _create_test_creature(health=0).is_alive is False
    assert _create_test_creature(health=10).is_alive is True
    assert _create_test_creature(health=-10).is_alive is False


def test_power_modifiers() -> None:
    assert _create_test_creature(claws=None, teeth=None).power_modifiers() == []
    assert _create_test_creature(claws=Claws.SMALL, teeth=None).power_modifiers() == [Claws.SMALL]
    assert _create_test_creature(claws=None, teeth=Teeth.LOW).power_modifiers() == [Teeth.LOW]
    assert _create_test_creature(claws=Claws.MEDIUM, teeth=Teeth.HIGH).power_modifiers() == [Claws.MEDIUM, Teeth.HIGH]


def test_movement_and_stamina() -> None:
    creature = _create_test_creature(stamina=2, num_wings=2)
    creature.position = 20
    creature.move(Fly())

    assert creature.stamina == 0
    assert creature.position == 28


def test_health() -> None:
    creature = _create_test_creature(health=100)
    creature.take_damage(15)
    assert creature.health == 85