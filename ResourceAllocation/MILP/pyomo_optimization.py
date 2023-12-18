from pyomo.environ import *

def solve_allocation_problem():
    # Criação do modelo
    model = ConcreteModel()

    # Conjunto de barcos
    barcos = ['jangadas', 'supercanoas', 'arcas']

    # Variáveis de decisão
    model.x = Var(barcos, domain=NonNegativeIntegers)

    # Função objetivo
    model.obj = Objective(expr=50 * model.x['jangadas'] + 70 * model.x['supercanoas'] + 100 * model.x['arcas'],
                          sense=maximize)

    # Restrições
    model.capitães = Constraint(expr=model.x['jangadas'] + model.x['supercanoas'] + model.x['arcas'] <= 10)
    model.tripulação = Constraint(expr=model.x['jangadas'] + 2 * model.x['supercanoas'] + 3 * model.x['arcas'] <= 18)
    model.jangadas_limit = Constraint(expr=model.x['jangadas'] <= 4)
    model.supercanoas_limit = Constraint(expr=model.x['supercanoas'] <= 8)
    model.arcas_limit = Constraint(expr=model.x['arcas'] <= 3)

    # Solver
    solver = SolverFactory('glpk')
    results = solver.solve(model)

    # Imprimindo resultados
    print('Jangadas:', round(value(model.x['jangadas'])))
    print('Supercanoas:', round(value(model.x['supercanoas'])))
    print('Arcas:', round(value(model.x['arcas'])))
    print('Lucro Total:', round(value(model.obj)))

if __name__ == "__main__":
    solve_allocation_problem()
