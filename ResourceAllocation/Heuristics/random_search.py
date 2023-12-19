import random


def random_search_allocation_problem(iterations=1000):
    best_profit = float('-inf')
    best_allocation = None

    for _ in range(iterations):
        rafts = random.randint(0, 4)
        super_canoes = random.randint(0, 8)
        cabins = random.randint(0, 3)

        # Applying constraints
        if rafts + super_canoes + cabins <= 10 and rafts + 2 * super_canoes + 3 * cabins <= 18:
            profit = 50 * rafts + 70 * super_canoes + 100 * cabins
            if profit > best_profit:
                best_profit = profit
                best_allocation = (rafts, super_canoes, cabins)

    # Printing results
    print('Rafts:', best_allocation[0])
    print('Super Canoes:', best_allocation[1])
    print('Cabins:', best_allocation[2])
    print('Total Profit:', best_profit)


if __name__ == "__main__":
    random_search_allocation_problem()
