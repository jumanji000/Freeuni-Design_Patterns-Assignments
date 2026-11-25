from dataclasses import dataclass

from simulation.movement import (
    DEFAULT_STRATEGIES,
    Crawl,
    Fly,
    Hop,
    Mover,
    Run,
    Walk
)


@dataclass
class _MovingCreature:
    stamina: int
    num_legs: int
    num_wings: int


def test_default_strategies_order() -> None:
    assert[type(s) for s in DEFAULT_STRATEGIES] == [Crawl, Hop, Walk, Run, Fly]


def test_crawl_requirements() -> None:
    crawl = Crawl()
    low_stamina: Mover = _MovingCreature(stamina=0, num_legs=0, num_wings=0)
    enough_stamina: Mover = _MovingCreature(stamina=1, num_legs=0, num_wings=0)

    assert crawl.can_perform(low_stamina) is False
    assert crawl.can_perform(enough_stamina) is True


def test_hop() -> None:
    assert Hop().can_perform(_MovingCreature(stamina=20, num_legs=1, num_wings=0)) is True
    assert Hop().can_perform(_MovingCreature(stamina=20, num_legs=0, num_wings=0)) is False
    assert Hop().can_perform(_MovingCreature(stamina=19, num_legs=1, num_wings=0)) is False


def test_walk() -> None:
    assert Walk().can_perform(_MovingCreature(stamina=40, num_legs=2, num_wings=0)) is True
    assert Walk().can_perform(_MovingCreature(stamina=40, num_legs=1, num_wings=0)) is False


def test_run() -> None:
    assert Run().can_perform(_MovingCreature(stamina=60, num_legs=2, num_wings=0)) is True
    assert Run().can_perform(_MovingCreature(stamina=60, num_legs=1, num_wings=0)) is False


def test_fly() -> None:
    assert Fly().can_perform(_MovingCreature(stamina=80, num_legs=0, num_wings=2)) is True
    assert Fly().can_perform(_MovingCreature(stamina=80, num_legs=0, num_wings=1)) is False