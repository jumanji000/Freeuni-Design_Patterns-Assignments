from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfiguration:
    num_runs: int = 100
    max_prey_position: int = 1000
    health_range: tuple[int, int] = (1, 200)
    stamina_range: tuple[int, int] = (0, 300)
    power_range: tuple[int, int] = (1, 10)
    max_num_legs: int = 4
    max_num_wings: int = 4
    part_evolve_chance: float = 0.7
