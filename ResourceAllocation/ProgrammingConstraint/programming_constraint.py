import click
from constraint import Problem


def solve_constraint():
    problem = Problem()

    # Decision variables
    problem.addVariable('rafts', range(5))  # 0 to 4
    problem.addVariable('super_canoes', range(9))  # 0 to 8
    problem.addVariable('cabins', range(4))  # 0 to 3

    # Objective function (maximizing profit)
    def maximize_profit(rafts, super_canoes, cabins):
        return - (50 * rafts + 70 * super_canoes + 100 * cabins)

    problem.addConstraint(maximize_profit, ('rafts', 'super_canoes', 'cabins'))

    # Captain and crew capacity constraints
    def captains_constraint(rafts, super_canoes, cabins):
        return rafts + super_canoes + cabins <= 10

    def crew_constraint(rafts, super_canoes, cabins):
        return rafts + 2 * super_canoes + 3 * cabins <= 18

    problem.addConstraint(captains_constraint, ('rafts', 'super_canoes', 'cabins'))
    problem.addConstraint(crew_constraint, ('rafts', 'super_canoes', 'cabins'))

    # Solving the problem
    solutions = problem.getSolutions()

    if solutions:
        # Finding the optimal solution
        best_solution = max(solutions, key=lambda x: -maximize_profit(x['rafts'], x['super_canoes'], x['cabins']))

        # Printing results
        print('Rafts:', best_solution['rafts'])
        print('Super Canoes:', best_solution['super_canoes'])
        print('Cabins:', best_solution['cabins'])
        print('Total Profit:', -maximize_profit(best_solution['rafts'], best_solution['super_canoes'], best_solution['cabins']))
    else:
        print('No solution found.')

if __name__ == "__main__":
    solve_constraint()

@click.command("programming_constraint")
def cli_programming_constraint():
    print("Run programming constraint")
    solve_constraint()