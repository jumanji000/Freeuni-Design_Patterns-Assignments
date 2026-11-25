from typing import Protocol


class Mover(Protocol):
    stamina: int
    num_legs: int
    num_wings: int


class MovementStrategy:
    name: str
    min_stamina_needed: int
    stamina_cost: int
    distance: int
    min_num_legs: int = 0
    min_num_wings: int = 0

    def can_perform(self, creature: Mover) -> bool:
        required_stamina = max(self.min_stamina_needed, self.stamina_cost)
        return (
            creature.stamina >= required_stamina
            and creature.num_legs >= self.min_num_legs
            and creature.num_wings >= self.min_num_wings
        )


class Crawl(MovementStrategy):
    name = "Crawl"
    min_stamina_needed = 0
    stamina_cost = 1
    distance = 1


class Hop(MovementStrategy):
    name = "Hop"
    min_stamina_needed = 20
    stamina_cost = 2
    distance = 3
    min_num_legs = 1


class Walk(MovementStrategy):
    name = "Walk"
    min_stamina_needed = 40
    stamina_cost = 2
    distance = 4
    min_num_legs = 2


class Run(MovementStrategy):
    name = "Run"
    min_stamina_needed = 60
    stamina_cost = 4
    distance = 6
    min_num_legs = 2


class Fly(MovementStrategy):
    name = "Fly"
    min_stamina_needed = 80
    stamina_cost = 4
    distance = 8
    min_num_wings = 2


DEFAULT_STRATEGIES: tuple[MovementStrategy, ...] = (
    Crawl(),
    Hop(),
    Walk(),
    Run(),
    Fly(),
)
