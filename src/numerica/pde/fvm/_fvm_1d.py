import numpy as np
from numerica.utils.ncfile import NcFile
from numerica.ode import time_integrator

def check_constraints(x_min, x_max, ncx, T, dtSave, cfl, initial_condition):

    if not (isinstance(x_min, (int, float)) and isinstance(x_max, (int, float))):
        raise ValueError("x_min and x_max must be numeric values.")
    if x_min >= x_max:
        raise ValueError("x_min must be less than x_max.")
    
    if not (isinstance(ncx, int) and ncx > 0):
        raise ValueError("ncx must be a positive integer.")
    
    if not (isinstance(T, (int, float)) and T > 0):
        raise ValueError("T must be a positive number.")
    
    if not (isinstance(dtSave, (int, float)) and dtSave > 0):
        raise ValueError("dtSave must be a positive number.")
    
    if not (isinstance(cfl, (int, float)) and cfl > 0):
        raise ValueError("cfl must be a positive number.")
    if 1 < cfl or cfl <= 0:
        raise ValueError("cfl must be in the range (0, 1].")
        
    if not callable(initial_condition):
        raise ValueError("initial_condition must be a callable function.")
    
def spatial_discretization(x_min, x_max, ncx):

    dx = (x_max - x_min) / ncx

    cell_centers = np.linspace(x_min + 0.5*dx, x_max - 0.5*dx, ncx)

    return cell_centers, dx

def computeTimeStep(U, cell_volume, cfl, lambda_max_function, current_time, final_time, tSave):

    # Compute maximum wave speed
    lambda_max = lambda_max_function(U)
    if not isinstance(lambda_max, (int, float, np.number)):
        raise ValueError("lambda_max_function(U) must return a scalar numeric value.")
    
    dt_cfl = cfl * cell_volume / lambda_max

    if (current_time + dt_cfl > final_time):

        dt = abs(final_time - current_time)

    elif (current_time + dt_cfl > tSave):

        dt = abs(tSave - current_time)

        if ((current_time + dt_cfl) > final_time):
            dt = abs(final_time - current_time)

    else:

        dt = dt_cfl

    return dt

def compute_mass(U, cell_volume):
    return np.sum(U * cell_volume)

def fvm_1d( x_min:float,
            x_max :float,
            ncx :int,
            T :float,
            dtSave :float,
            ic:callable,
            cfl :float,
            lambda_max_function:callable,
            physical_flux_function:callable,
            numerical_flux_function:callable,
            filename:str,
            title:str,
            logging:bool = False,
            description:str = '',
            references:str = ''):
    """
    Finite Volume Method for 1D Hyperbolic PDEs.

    """

    check_constraints(x_min, x_max, ncx, T, dtSave, cfl, ic)

    cell_centers, dx = spatial_discretization(x_min, x_max, ncx)

    # Create NetCDF file
    ncfile = NcFile(filename, title, description=description, references=references)
    ncfile.addCoords({'x': cell_centers})
    ncfile.addVars(['u'])

    # Initial condition
    U = ic(cell_centers)
    ncfile.save(0.0, {'u': U})

    # Time-stepping loop
    t = 0.0
    n = 1
    tSave = dtSave

    if logging:
        print(f"Starting simulation...")
        print("Initial parameters:")
        print(f"  left_boundary: {x_min}")
        print(f"  right_boundary: {x_max}")
        print(f"  number_of_cells: {ncx}")
        print(f"  final_time: {T}")
        print(f"  save_interval: {dtSave}")
        print(f"  cfl: {cfl}")
    
    while (t < T):

        if logging: log = ''

        dt = computeTimeStep(U, dx, cfl, lambda_max_function, t, T, tSave)
        if logging: log += f"Iteration {n} | dt: {dt:.4e} |"

        F_star = numerical_flux_function(U, physical_flux_function)

        F = -(F_star[1:] - F_star[:-1]) / dx
        
        U = time_integrator.euler(dt, U, F)
        if logging: log += f" mass: {compute_mass(U, dx):.4e} |"

        t += dt
        if logging: log += f" t: {t:.4e} |"
        n += 1

        if (abs(t - tSave) < 1e-12 or abs(t - T) < 1e-12):
            ncfile.save(t, {"u": U})
            tSave += dtSave
            if logging: log += " [saved]"

        if logging: print(log)
