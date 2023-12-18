from pulp import *

# Criação do problema de maximização
prob = LpProblem("Maximize_Profit", LpMaximize)

# Variáveis de decisão
jangadas = LpVariable("Jangadas", lowBound=0, cat='Integer')
supercanoas = LpVariable("Supercanoas", lowBound=0, cat='Integer')
arcas = LpVariable("Arcas", lowBound=0, cat='Integer')

# Função objetivo
prob += 50 * jangadas + 70 * supercanoas + 100 * arcas, "Total_Profit"

# Restrições
prob += jangadas <= 4
prob += supercanoas <= 8
prob += arcas <= 3
prob += jangadas + supercanoas + arcas <= 10  # Capitães
prob += jangadas + 2*supercanoas + 3*arcas <= 18  # Tripulação

# Resolvendo o problema
prob.solve()

# Imprimindo resultados
print("Jangadas:", value(jangadas))
print("Supercanoas:", value(supercanoas))
print("Arcas:", value(arcas))
print("Lucro Total:", value(prob.objective))
