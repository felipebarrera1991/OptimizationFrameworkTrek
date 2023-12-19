from ortools.linear_solver import pywraplp


def solve_allocation_problem():
    # Creating the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Decision variables
    rafts = solver.IntVar(0, 4, 'Rafts')
    super_canoes = solver.IntVar(0, 8, 'Super Canoes')
    cabins = solver.IntVar(0, 3, 'Cabins')

    # Objective function
    objective = solver.Objective()
    objective.SetCoefficient(rafts, 50)
    objective.SetCoefficient(super_canoes, 70)
    objective.SetCoefficient(cabins, 100)
    objective.SetMaximization()

    # Constraints
    solver.Add(rafts + super_canoes + cabins <= 10)  # Captains
    solver.Add(rafts + 2 * super_canoes + 3 * cabins <= 18)  # Crew

    # Solving the problem
    solver.Solve()

    # Printing results
    print('Rafts:', rafts.solution_value())
    print('Super Canoes:', super_canoes.solution_value())
    print('Cabins:', cabins.solution_value())
    print('Total Profit:', objective.Value())

if __name__ == "__main__":
    solve_allocation_problem()
