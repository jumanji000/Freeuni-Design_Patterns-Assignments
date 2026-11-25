import pytest

from simulation.configuration import SimulationConfiguration


def test_default_configuration() -> None:
    configuration = SimulationConfiguration()

    assert configuration.num_runs == 100
    assert configuration.max_prey_position == 1000
    assert configuration.health_range == (1, 200)
    assert configuration.stamina_range == (0, 300)
    assert configuration.power_range == (1, 10)
    assert configuration.max_num_legs == 4
    assert configuration.max_num_wings == 4
    assert configuration.part_evolve_chance == 0.7


def test_custom_configuration() -> None:
    configuration = SimulationConfiguration(
        num_runs=5,
        max_prey_position=100,
        health_range=(10, 20),
        stamina_range=(15, 30),
        power_range=(2, 6),
        max_num_legs=2,
        max_num_wings=1,
        part_evolve_chance=0.33
    )

    assert configuration.num_runs == 5
    assert configuration.max_prey_position == 100
    with pytest.raises(AttributeError):
        setattr(configuration, "health_range", (1, 3333))