import click
import random

from simanneal import Annealer


class AllocationProblem(Annealer):
    def __init__(self, state):
        super(AllocationProblem, self).__init__(state)

    def move(self):
        rafts = random.randint(0, 4)
        super_canoes = random.randint(0, 8)
        cabins = random.randint(0, 3)

        # Applying constraints
        if rafts + super_canoes + cabins <= 10 and rafts + 2 * super_canoes + 3 * cabins <= 18:
            self.state = (rafts, super_canoes, cabins)

    def energy(self):
        rafts, super_canoes, cabins = self.state
        return -(50 * rafts + 70 * super_canoes + 100 * cabins)


def simulated_annealing_allocation_problem():
    initial_state = (0, 0, 0)
    allocation_problem = AllocationProblem(initial_state)
    allocation_problem.set_schedule(allocation_problem.auto(minutes=0.1))  
    allocation_problem.steps = 1000  # Number of iterations
    allocation_problem.anneal()

    # Printing results
    print('Rafts:', allocation_problem.state[0])
    print('Super Canoes:', allocation_problem.state[1])
    print('Cabins:', allocation_problem.state[2])
    print('Total Profit:', -allocation_problem.energy())


if __name__ == "__main__":
    simulated_annealing_allocation_problem()

@click.command("simulated_annealing")
def cli_simulated_annealing():
    print("Run simulated annealing")
    simulated_annealing_allocation_problem()