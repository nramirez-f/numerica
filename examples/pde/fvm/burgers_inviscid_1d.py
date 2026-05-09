import numpy as np
from numerica.pde.fvm.models import burgers_inviscid_1d

"""
This example demonstrates how to solve the 1D burgers inviscid equation 

u_t + u u_x = 0

using the finite volume method (FVM) with the Numerica library.

The 1D Burgers inviscid equation is a fundamental partial differential equation that
describes the evolution of a scalar quantity under nonlinear advection.
"""

def gaussian_pulse(x):
    return 4 * np.exp(-(x - 4.0)**2)

burgers_inviscid_1d(left_boundary=0.0,
                    right_boundary=12.0,
                    number_of_cells=5000,
                    final_time=24.0,
                    save_interval=0.1,
                    initial_condition=gaussian_pulse)
