from ortools.linear_solver import pywraplp

def solve_allocation_problem():
    # Criação do solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variáveis de decisão
    jangadas = solver.IntVar(0, 4, 'Jangadas')
    supercanoas = solver.IntVar(0, 8, 'Supercanoas')
    arcas = solver.IntVar(0, 3, 'Arcas')

    # Função objetivo
    objective = solver.Objective()
    objective.SetCoefficient(jangadas, 50)
    objective.SetCoefficient(supercanoas, 70)
    objective.SetCoefficient(arcas, 100)
    objective.SetMaximization()

    # Restrições
    solver.Add(jangadas + supercanoas + arcas <= 10)  # Capitães
    solver.Add(jangadas + 2 * supercanoas + 3 * arcas <= 18)  # Tripulação

    # Resolvendo o problema
    solver.Solve()

    # Imprimindo resultados
    print('Jangadas:', jangadas.solution_value())
    print('Supercanoas:', supercanoas.solution_value())
    print('Arcas:', arcas.solution_value())
    print('Lucro Total:', objective.Value())

if __name__ == "__main__":
    solve_allocation_problem()