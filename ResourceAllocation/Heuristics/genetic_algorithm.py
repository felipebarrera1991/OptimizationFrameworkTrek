import random
from deap import base, creator, tools

# Definição do problema
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def evaluate(individual):
    jangadas, supercanoas, arcas = individual
    return 50 * jangadas + 70 * supercanoas + 100 * arcas,

toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, 0, 4)  # 0 a 4 para jangadas e 0 a 8 para supercanoas e 0 a 3 para arcas
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=4, indpb=0.5)
toolbox.register("select", tools.selTournament, tournsize=3)

def genetic_algorithm_allocation_problem():
    population = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40  # Probabilidade de crossover, probabilidade de mutação, número de gerações

    # Avaliação da população inicial
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    for gen in range(NGEN):
        # Seleção dos indivíduos para reprodução
        offspring = toolbox.select(population, len(population))

        # Clone dos indivíduos selecionados
        offspring = list(map(toolbox.clone, offspring))

        # Aplicação de crossover e mutação nos indivíduos selecionados
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Avaliação dos indivíduos com fitness invalidada
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Atualização da população
        population[:] = offspring

    # Obtendo o melhor indivíduo da última população
    best_individual = tools.selBest(population, 1)[0]

    # Imprimindo resultados
    print('Jangadas:', best_individual[0])
    print('Supercanoas:', best_individual[1])
    print('Arcas:', best_individual[2])
    print('Lucro Total:', -best_individual.fitness.values[0])

if __name__ == "__main__":
    genetic_algorithm_allocation_problem()
