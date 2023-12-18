import random

def random_search_allocation_problem(iterations=1000):
    best_profit = float('-inf')
    best_allocation = None

    for _ in range(iterations):
        jangadas = random.randint(0, 4)
        supercanoas = random.randint(0, 8)
        arcas = random.randint(0, 3)

        # Aplicando restrições
        if jangadas + supercanoas + arcas <= 10 and jangadas + 2 * supercanoas + 3 * arcas <= 18:
            profit = 50 * jangadas + 70 * supercanoas + 100 * arcas
            if profit > best_profit:
                best_profit = profit
                best_allocation = (jangadas, supercanoas, arcas)

    # Imprimindo resultados
    print('Jangadas:', best_allocation[0])
    print('Supercanoas:', best_allocation[1])
    print('Arcas:', best_allocation[2])
    print('Lucro Total:', best_profit)

if __name__ == "__main__":
    random_search_allocation_problem()
