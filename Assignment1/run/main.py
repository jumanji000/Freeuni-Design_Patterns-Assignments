from simulation.combat import PowerCalculator, SimultaneousRound
from simulation.configuration import SimulationConfiguration
from simulation.engine import Simulation
from simulation.factory import CreatureFactory
from simulation.movement_strategy_selectors import GreedyStrategy
from simulation.phases import ChasePhase, FightPhase
from simulation.reporting import ConsoleReporter, ResultCounter


def main() -> None:
    configuration = SimulationConfiguration()
    reporter = ConsoleReporter()
    counter = ResultCounter()

    simulation = Simulation(
        factory=CreatureFactory(configuration),
        chase=ChasePhase(GreedyStrategy()),
        fight=FightPhase(SimultaneousRound(PowerCalculator())),
        listeners=[reporter, counter],
    )

    for simulation_id in range(1, configuration.num_runs + 1):
        simulation.run_simulation(simulation_id)

    reporter.print_all_simulation_summary(counter.counts, configuration.num_runs)


if __name__ == "__main__":
    main()
