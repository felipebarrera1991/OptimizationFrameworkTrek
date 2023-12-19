import random

from deap import base, creator, tools

# Problem definition
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def evaluate(individual):
    rafts, super_canoes, cabins = individual
    return 50 * rafts + 70 * super_canoes + 100 * cabins,

toolbox = base.Toolbox()
# 0 to 4 for rafts and 0 to 8 for super canoes and 0 to 3 for cabins
toolbox.register("attr_int", random.randint, 0, 4)  
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=4, indpb=0.5)
toolbox.register("select", tools.selTournament, tournsize=3)

def genetic_algorithm_allocation_problem():
    population = toolbox.population(n=50)
    # Crossover probability, mutation probability, number of generations
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40  

    # Initial population evaluation
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    for gen in range(NGEN):
        # Selection of individuals for reproduction
        offspring = toolbox.select(population, len(population))

        # Cloning selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Applying crossover and mutation to selected individuals
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluating individuals with invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Updating the population
        population[:] = offspring

    # Getting the best individual from the last population
    best_individual = tools.selBest(population, 1)[0]

    # Printing results
    print('Rafts:', best_individual[0])
    print('Super Canoes:', best_individual[1])
    print('Cabins:', best_individual[2])
    print('Total Profit:', -best_individual.fitness.values[0])

if __name__ == "__main__":
    genetic_algorithm_allocation_problem()
