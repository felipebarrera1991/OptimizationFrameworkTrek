

# Resource Allocation Problem - README

## Problem Description
Captain Caveman Inc., located in Stone Age, rents out three types of boats for maritime tours: rafts, super-canoes, and cabins with crews. The company provides a captain to navigate each boat along with a crew, varying based on the boat type: one for rafts, two for super-canoes, and three for cabins. The company owns 4 rafts, 8 super-canoes, and 3 cabins. They have 10 captains and 18 crew members. Rent is charged on a daily basis, earning $50 per raft, $70 per super-canoe, and $100 per cabin. The goal is to create an optimization model that determines the rental scheme maximizing profit.

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
