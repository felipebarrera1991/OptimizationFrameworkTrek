# OptimizationFrameworkTrek
"OptimizationFrameworkTrek" explores MILP optimization using Pulp, Gurobi, OR-Tools, Pyomo, and LocalSolver Frameworks. Dive into route optimization problems with synthetic data, comparing coding efficiency and performance across frameworks. Uncover optimization capabilities in this curated collection for data scientists and enthusiasts

---

# Setting up Conda Environment for Project

## Environment Setup Instructions

1. **Clone the Project Repository**
    ```bash
    git clone <project_repository_url>
    cd <project_directory>
    ```

2. **Create a Conda Environment**
    ```bash
    conda env create -f environment.yml
    conda activate optimization
    ```

3. **Verification**
    Verify that the environment has been set up correctly:
    ```bash
    conda env list
    ```

4. **Start Working**
    You can now start working within the newly created Conda environment for the project.

5. **Run Optimization**
    ```bash
    ./run cli_genetic_algorithm
    ./run cli_random_search
    ./run cli_simulated_annealing
    ./run cli_ortools_optimization
    ./run cli_pulp_optimization
    ./run cli_pyomo_optimization
    ./run cli_programming_constraint
    ```

# Installing CBC and GLPK Solvers for Pyomo

## Overview
CBC (Coin-or Branch and Cut) and GLPK (GNU Linear Programming Kit) are open-source linear programming solvers commonly used with Pyomo. Here's how to install them.

## Installation Steps

### Using Conda
1. **Open Terminal or Command Prompt**
   
2. **Install CBC and GLPK**
   
    ```
    conda install -c conda-forge coincbc glpk
    ```

3. **Verification**
   
    To verify that the solvers have been installed successfully, you can check the list of installed packages:
   
    ```
    conda list
    ```

4. **Usage with Pyomo**
   
    Once installed, you can utilize these solvers with Pyomo by specifying them as the solver in your optimization models.

## Pyomo Configuration
To use CBC or GLPK as solvers within your Pyomo optimization models, you can specify them during the solver configuration in your Python code.

For CBC:

```python
from pyomo.environ import SolverFactory

solver = SolverFactory('cbc')
