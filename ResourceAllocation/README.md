

# Resource Allocation Problem - README

## Problem Description
Captain Caveman Inc., located in Stone Age, rents out three types of boats for maritime tours: rafts, super-canoes, and cabins with crews. The company provides a captain to navigate each boat along with a crew, varying based on the boat type: one for rafts, two for super-canoes, and three for cabins. The company owns 4 rafts, 8 super-canoes, and 3 cabins. They have 10 captains and 18 crew members. Rent is charged on a daily basis, earning $50 per raft, $70 per super-canoe, and $100 per cabin. The goal is to create an optimization model that determines the rental scheme maximizing profit.

### Mathematical Formulation:

**Parameters:**
- $$\(J\)$$ = Set of rafts
- $$\(S\)$$ = Set of super canoes
- $$\(A\)$$ = Set of cabins
- $$\(P_j\)$$ = Profit per raft
- $$\(P_s\)$$ = Profit per super canoe
- $$\(P_a\)$$ = Profit per cabin
- $$\(C_j\)$$ = Captain capacity per raft
- $$\(C_s\)$$ = Captain capacity per super canoe
- $$\(C_a\)$$ = Captain capacity per cabin
- $$\(T_j\)$$ = Crew per raft
- $$\(T_s\)$$ = Crew per super canoe
- $$\(T_a\)$$ = Crew per cabin

**Decision Variables:**
- $$\(x_j\)$$ = Quantity of rafts to allocate
- $$\(x_s\)$$ = Quantity of super canoes to allocate
- $$\(x_a\)$$ = Quantity of cabins to allocate

**Objective:**
Maximize the total profit $$\(L\)$$ represented by the sum of the profit of each type of allocated boat.

$$\[ L = P_j \cdot x_j + P_s \cdot x_s + P_a \cdot x_a \]$$

**Constraints:**
- Captain capacity:
$$\[ C_j \cdot x_j + C_s \cdot x_s + C_a \cdot x_a \leq \text{Total Captain Capacity} \]$$
- Crew:
$$\[ T_j \cdot x_j + T_s \cdot x_s + T_a \cdot x_a \leq \text{Total Crew Capacity} \]$$
- Maximum quantity constraints for each type of boat:
$$\[ x_j \leq \text{Maximum Quantity of Rafts} \]$$
$$\[ x_s \leq \text{Maximum Quantity of Super Canoes} \]$$
$$\[ x_a \leq \text{Maximum Quantity of Cabins} \]$$

This problem aims to allocate rafts, super canoes, and cabins to maximize the total profit while respecting the captain and crew capacities for each type of boat.

## Approaches Used

### MILP Modeling
We utilized the PuLP library, OR-Tools, and other optimization libraries to model the problem as a Mixed-Integer Linear Program (MILP). This involved formulating variables, constraints, and an objective function to find the optimal solution.

### Constraint Programming Approach
We used the python-constraint library to model the problem with constraints on captain availability, crew capacity, and profit maximization. Constraint programming was explored to find feasible solutions.

### Heuristic: Simulated Annealing/Genetic Algorithm
We explored libraries such as simanneal or DEAP to implement heuristics like Simulated Annealing or Genetic Algorithms, aiming to find approximate solutions for the resource allocation problem.

## Optimization Libraries Utilized
- PuLP: Used to solve linear and integer optimization problems.
- OR-Tools: Offers solvers for various problems including linear programming, integer programming, and more.
- Pyomo: Open-source optimization modeling language that facilitates the formulation and solution of complex optimization problems in python.
- python-constraint: Utilized for modeling constraint satisfaction problems.
- simanneal: Implementation of the Simulated Annealing algorithm in Python.
- DEAP: Library for evolutionary algorithms in Python, including Genetic Algorithms.

Each approach was implemented in individual scripts (e.g., model_pulp.py, model_constraint.py) and analyzed to find the best resource allocation maximizing profit for Captain Caveman Inc.

For more details on implementations and solvers used, check the respective Python scripts in this repository.