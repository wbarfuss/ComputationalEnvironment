# AUTOGENERATED! DO NOT EDIT! File to edit: ../HeavyComputations.ipynb.

# %% auto 0
__all__ = ['noisy_predprey_model']

# %% ../HeavyComputations.ipynb 5
import numpy as np

# %% ../HeavyComputations.ipynb 6
def noisy_predprey_model(prey_birth_rate, 
                         prey_mortality, 
                         predator_efficiency, 
                         predator_death_rate,
                         initial_prey, 
                         initial_predators,
                         time_length,
                         noiselevel):
    """ Discrete-time predator-prey model. """
    x = -1 * np.ones(time_length)
    y = -1 * np.ones(time_length)
    x[0] = initial_prey
    y[0] = initial_predators
    for t in range(1, time_length):
        x[t] = x[t-1] + prey_birth_rate * x[t-1]\
            - prey_mortality * y[t-1]*x[t-1]
        y[t] = y[t-1] + predator_efficiency * y[t-1]*x[t-1]\
            - predator_death_rate * y[t-1]\
            + noiselevel * (0.5 - np.random.rand())
    return x, y
