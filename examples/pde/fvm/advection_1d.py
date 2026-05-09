import numpy as np
from numerica.pde.fvm.models import advection_1d

"""
This example demonstrates how to solve the 1D advection equation 

u_t + c u_x = 0

using the finite volume method (FVM) with the Numerica library.

The advection equation is a fundamental partial differential equation that 
describes the transport of a quantity by a constant velocity field. 
"""

def gaussian_pulse(x):
    return np.exp(-(x - 4.0)**2)

advection_1d(left_boundary=0.0,
             right_boundary=12.0,
             number_of_cells=1000,
             final_time=12.0,
             save_interval=0.2,
             initial_condition=gaussian_pulse,
             velocity=1.0)
