from simulation.combat import PowerCalculator, SimultaneousRound
from simulation.creature import Creature
from simulation.movement import Crawl, MovementStrategy, Mover
from simulation.movement_strategy_selectors import GreedyStrategy, MovementSelector
from simulation.phases import ChasePhase, FightPhase
from simulation.result import Result


class _FixedSelector(MovementSelector):
    def __init__(self, strategy: MovementStrategy | None) -> None:
        self._strategy = strategy

    def choose_movement(self, creature: Mover) -> MovementStrategy | None:
        if self._strategy is None or not self._strategy.can_perform(creature):
            return None
        return self._strategy


def _make_creature(role: str, position: int, health: int, stamina: int) -> Creature:
    return Creature(
        role=role,
        position=position,
        health=health,
        stamina=stamina,
        attack_power=10,
        num_legs=2,
        num_wings=0,
    )


def test_chase_phase_catches_prey() -> None:
    predator = _make_creature("Predator", position=0, health=100, stamina=50)
    prey = _make_creature("Prey", position=2, health=100, stamina=0)

    caught = ChasePhase(GreedyStrategy()).run(predator, prey)

    assert caught is True
    assert predator.position >= prey.position


def test_chase_phase_returns_false_when_predator_cannot_move() -> None:
    predator = _make_creature("Predator", position=0, health=100, stamina=0)
    prey = _make_creature("Prey", position=10, health=100, stamina=50)

    caught = ChasePhase(_FixedSelector(Crawl())).run(predator, prey)

    assert caught is False


def test_fight_phase_outcomes() -> None:
    resolver = SimultaneousRound(PowerCalculator())
    fight = FightPhase(resolver)

    strong_pred = _make_creature("Predator", position=0, health=100, stamina=10)
    strong_pred.attack_power = 50
    weak_prey = _make_creature("Prey", position=0, health=20, stamina=10)
    weak_prey.attack_power = 1
    assert fight.run(strong_pred, weak_prey) == Result.FIGHT_HAPPENED

    weak_pred = _make_creature("Predator", position=0, health=10, stamina=10)
    weak_pred.attack_power = 1
    strong_prey = _make_creature("Prey", position=0, health=100, stamina=10)
    strong_prey.attack_power = 50
    assert fight.run(weak_pred, strong_prey) == Result.PREY_ESCAPED