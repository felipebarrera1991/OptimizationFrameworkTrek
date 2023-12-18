from constraint import Problem

def solve_constraint():
    problem = Problem()

    # Variáveis de decisão
    problem.addVariable('jangadas', range(5))  # 0 a 4
    problem.addVariable('supercanoas', range(9))  # 0 a 8
    problem.addVariable('arcas', range(4))  # 0 a 3

    # Função objetivo (maximizar o lucro)
    def maximize_profit(jangadas, supercanoas, arcas):
        return - (50 * jangadas + 70 * supercanoas + 100 * arcas)

    problem.addConstraint(maximize_profit, ('jangadas', 'supercanoas', 'arcas'))

    # Restrições de capacidade de capitães e tripulação
    def captains_constraint(jangadas, supercanoas, arcas):
        return jangadas + supercanoas + arcas <= 10

    def crew_constraint(jangadas, supercanoas, arcas):
        return jangadas + 2 * supercanoas + 3 * arcas <= 18

    problem.addConstraint(captains_constraint, ('jangadas', 'supercanoas', 'arcas'))
    problem.addConstraint(crew_constraint, ('jangadas', 'supercanoas', 'arcas'))

    # Resolvendo o problema
    solutions = problem.getSolutions()

    if solutions:
        # Encontrando a solução ótima
        best_solution = max(solutions, key=lambda x: -maximize_profit(x['jangadas'], x['supercanoas'], x['arcas']))

        # Imprimindo resultados
        print('Jangadas:', best_solution['jangadas'])
        print('Supercanoas:', best_solution['supercanoas'])
        print('Arcas:', best_solution['arcas'])
        print('Lucro Total:', -maximize_profit(best_solution['jangadas'], best_solution['supercanoas'], best_solution['arcas']))
    else:
        print('Não foi encontrada uma solução.')

if __name__ == "__main__":
    solve_constraint()
