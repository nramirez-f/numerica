import numpy as np
import netCDF4 as nc
import time
from . import time_integrator

def check_constraints(F, t0, U0, T, dt):
    if dt > T:
        raise ValueError(f"Time step dt={dt} is larger than total time T={T}. Please choose a smaller dt.")
    if t0 < 0:
        raise ValueError(f"Initial time t0={t0} must be non-negative.")
    if T <= t0:
        raise ValueError(f"Total time T={T} must be greater than initial time t0={t0}.")
    if not callable(F):
        raise ValueError("F must be a callable function that takes (t, U) as arguments.")


def euler(F, t0, U0, T, dt,
          filepath=None, iter_name='time', iter_unit='s', var_name='u'):

    check_constraints(F, t0, U0, T, dt)

    # Detect if input is scalar and normalize to array
    is_scalar = np.ndim(U0) == 0
    U = np.atleast_1d(np.asarray(U0, dtype=float))
    m = len(U)  # number of variables in the system

    # Create wrapper function that handles both scalar and vector cases
    def Fvec(t, U):
        y = F(t, U[0] if is_scalar else U)
        return np.atleast_1d(np.asarray(y, dtype=float))

    # Create NetCDF file and variables
    if filepath:
        ncfile = nc.Dataset(filepath, 'w', format='NETCDF4')
        ncfile.history = 'Created at ' + time.ctime(time.time())
        ncfile.source = 'Numerica Library'
        ncfile.description = 'Euler method for ODE integration'
        ncfile.createDimension(iter_name, None)
        ncfile.createVariable(iter_name, 'f8', (iter_name,)).units = iter_unit
        if is_scalar:
            ncfile.createVariable(var_name, 'f8', (iter_name,))
        for i in range(m):
            ncfile.createVariable(var_name + str(i), 'f8', (iter_name,))

    # Save initial condition
    if filepath:
        ncfile.variables[iter_name][0] = t0
        if is_scalar:
            ncfile.variables[var_name][0] = U[0]
        else:
            for i in range(m):
                ncfile.variables[var_name + str(i)][0] = U[i]

    n = 0
    t = t0
    while t < T:
        h = min(dt, T - t)
        
        U = time_integrator.euler(h, U, Fvec, t)

        n += 1
        t += h

        # Save results to file
        if filepath:
            ncfile.variables[iter_name][n] = t
            if is_scalar:
                ncfile.variables[var_name][n] = U[0]
            else:
                for i in range(m):
                    ncfile.variables[var_name + str(i)][n] = U[i]

    if filepath:
        ncfile.close()

    # Return scalar if input was scalar, otherwise return array
    return U[0] if is_scalar else U
