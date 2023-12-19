from pulp import *

# Creating the maximization problem
prob = LpProblem("Maximize_Profit", LpMaximize)

# Decision variables
rafts = LpVariable("Rafts", lowBound=0, cat='Integer')
super_canoes = LpVariable("Super Canoes", lowBound=0, cat='Integer')
cabins = LpVariable("Cabins", lowBound=0, cat='Integer')

# Objective function
prob += 50 * rafts + 70 * super_canoes + 100 * cabins, "Total_Profit"

# Constraints
prob += rafts <= 4
prob += super_canoes <= 8
prob += cabins <= 3
prob += rafts + super_canoes + cabins <= 10  # Captains
prob += rafts + 2 * super_canoes + 3 * cabins <= 18  # Crew

# Solving the problem
prob.solve()

# Printing results
print("Rafts:", value(rafts))
print("Super Canoes:", value(super_canoes))
print("Cabins:", value(cabins))
print("Total Profit:", value(prob.objective))
