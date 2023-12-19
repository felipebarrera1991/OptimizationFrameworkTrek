import click
from pyomo.environ import *


def solve_allocation_problem_pyomo():
    # Creating the model
    model = ConcreteModel()

    # Set of boats
    boats = ['rafts', 'super_canoes', 'cabins']

    # Decision variables
    model.x = Var(boats, domain=NonNegativeIntegers)

    # Objective function
    model.obj = Objective(expr=50 * model.x['rafts'] + 70 * model.x['super_canoes'] + 100 * model.x['cabins'],
                          sense=maximize)

    # Constraints
    model.captains = Constraint(expr=model.x['rafts'] + model.x['super_canoes'] + model.x['cabins'] <= 10)
    model.crew = Constraint(expr=model.x['rafts'] + 2 * model.x['super_canoes'] + 3 * model.x['cabins'] <= 18)
    model.rafts_limit = Constraint(expr=model.x['rafts'] <= 4)
    model.super_canoes_limit = Constraint(expr=model.x['super_canoes'] <= 8)
    model.cabins_limit = Constraint(expr=model.x['cabins'] <= 3)

    # Solver
    solver = SolverFactory('glpk')
    results = solver.solve(model)

    # Printing results
    print('Rafts:', round(value(model.x['rafts'])))
    print('Super Canoes:', round(value(model.x['super_canoes'])))
    print('Cabins:', round(value(model.x['cabins'])))
    print('Total Profit:', round(value(model.obj)))


@click.command("pyomo_optimization")
def cli_pyomo_optimization():
    print("Run pyomo optimization")
    solve_allocation_problem_pyomo()