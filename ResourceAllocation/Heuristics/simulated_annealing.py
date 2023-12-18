from simanneal import Annealer
import random

class AllocationProblem(Annealer):
    def __init__(self, state):
        super(AllocationProblem, self).__init__(state)

    def move(self):
        jangadas = random.randint(0, 4)
        supercanoas = random.randint(0, 8)
        arcas = random.randint(0, 3)

        # Aplicando restrições
        if jangadas + supercanoas + arcas <= 10 and jangadas + 2 * supercanoas + 3 * arcas <= 18:
            self.state = (jangadas, supercanoas, arcas)

    def energy(self):
        jangadas, supercanoas, arcas = self.state
        return -(50 * jangadas + 70 * supercanoas + 100 * arcas)

def simulated_annealing_allocation_problem():
    initial_state = (0, 0, 0)
    allocation_problem = AllocationProblem(initial_state)
    allocation_problem.set_schedule(allocation_problem.auto(minutes=0.1))  # Ajuste dos parâmetros conforme necessário
    allocation_problem.steps = 1000  # Número de iterações
    allocation_problem.anneal()

    # Imprimindo resultados
    print('Jangadas:', allocation_problem.state[0])
    print('Supercanoas:', allocation_problem.state[1])
    print('Arcas:', allocation_problem.state[2])
    print('Lucro Total:', -allocation_problem.energy())

if __name__ == "__main__":
    simulated_annealing_allocation_problem()
