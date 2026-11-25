from dataclasses import dataclass

from simulation.movement import Crawl, Fly, Hop, Mover, Run, Walk
from simulation.movement_strategy_selectors import GreedyStrategy, StaminaSaverStrategy


@dataclass
class MovingCreature:
    stamina: int
    num_legs: int
    num_wings: int


def test_greedy_strategy() -> None:
    selector = GreedyStrategy()
    capable_to_move: Mover = MovingCreature(stamina=100, num_legs=2, num_wings=2)
    stuck: Mover = MovingCreature(stamina=0, num_legs=0, num_wings=0)

    chosen = selector.choose_movement(capable_to_move)
    assert isinstance(chosen, Fly)
    assert selector.choose_movement(stuck) is None


def test_stamina_saver_strategy() -> None:
    selector = StaminaSaverStrategy()
    capable_to_move: Mover = MovingCreature(stamina=100, num_legs=2, num_wings=2)

    chosen = selector.choose_movement(capable_to_move)
    assert isinstance(chosen, Crawl)

    walk_selector = StaminaSaverStrategy(strategies=(Walk(), Hop(), Run()))
    assert isinstance(walk_selector.choose_movement(capable_to_move), Walk)

    hop_selector = StaminaSaverStrategy(strategies=(Hop(), Run()))
    assert isinstance(hop_selector.choose_movement(capable_to_move), Hop)