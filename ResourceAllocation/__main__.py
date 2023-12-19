import click

from ResourceAllocation.Heuristics.genetic_algorithm import cli_genetic_algorithm
from ResourceAllocation.Heuristics.random_search import cli_random_search
from ResourceAllocation.Heuristics.simulated_annealing import cli_simulated_annealing
from ResourceAllocation.MILP.ortools_optimization import cli_ortools_optimization
from ResourceAllocation.MILP.pulp_optimization import cli_pulp_optimization
from ResourceAllocation.MILP.pyomo_optimization import cli_pyomo_optimization
from ResourceAllocation.ProgrammingConstraint.programming_constraint import cli_programming_constraint

@click.group("main")
def main():
    """Run all optimization approach for single or multiple cases"""
    pass

main.add_command(cli_genetic_algorithm)
main.add_command(cli_random_search)
main.add_command(cli_simulated_annealing)
main.add_command(cli_ortools_optimization)
main.add_command(cli_pulp_optimization)
main.add_command(cli_pyomo_optimization)
main.add_command(cli_programming_constraint)

main()