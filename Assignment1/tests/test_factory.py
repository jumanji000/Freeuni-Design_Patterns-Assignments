import random

from simulation.body_parts import Claws, Teeth
from simulation.configuration import SimulationConfiguration
from simulation.factory import CreatureFactory


def test_factory_creates_predator_and_prey_with_seeded_rng() -> None:
    config = SimulationConfiguration(
        max_prey_position=250,
        health_range=(20, 40),
        stamina_range=(10, 30),
        power_range=(2, 5),
        max_num_legs=3,
        max_num_wings=2,
        part_evolve_chance=1.0,
    )
    factory = CreatureFactory(config, rng=random.Random(42))

    predator = factory.create_predator()
    prey = factory.create_prey()

    assert predator.role == "Predator"
    assert predator.position == 0
    assert 20 <= predator.health <= 40
    assert 10 <= predator.stamina <= 30
    assert 2 <= predator.attack_power <= 5
    assert 0 <= predator.num_legs <= 3
    assert 0 <= predator.num_wings <= 2
    assert isinstance(predator.claws, Claws)
    assert isinstance(predator.teeth, Teeth)

    assert prey.role == "Prey"
    assert 0 <= prey.position <= 250


def test_factory_part_evolve_chance_zero_produces_none() -> None:
    config = SimulationConfiguration(part_evolve_chance=0.0)
    factory = CreatureFactory(config, rng=random.Random(0))

    predator = factory.create_predator()
    assert predator.claws is None
    assert predator.teeth is None


def test_factory_default_rng_works() -> None:
    factory = CreatureFactory(SimulationConfiguration())
    predator = factory.create_predator()
    assert predator.role == "Predator"