import numpy as np
import netCDF4 as nc
import time

def compute_F(F, t, U, is_scalar):
    return np.atleast_1d(np.asarray(F(t, U[0] if is_scalar else U), dtype=float))

def euler(F,t0,U0,T,dt,
          filepath=None,iter_name='t',iter_unit='s',var_name='u'):

    # for scalar ODES
    is_scalar = np.ndim(U0) == 0
    U = np.atleast_1d(np.asarray(U0, dtype=float))

    m = len(U) # number of variables in the system

    # Create NetCDF file and variables
    if (filepath):
        ncfile = nc.Dataset(filepath, 'w', format='NETCDF4')
        ncfile.history = 'Created at ' + time.ctime(time.time())
        ncfile.source = 'Numerica Library'
        ncfile.description = 'Euler method for ODE integration'
        ncfile.createDimension(iter_name, None)
        ncfile.createVariable(iter_name, 'f8', (iter_name,)).units = iter_unit
        if (is_scalar):
            ncfile.createVariable(var_name, 'f8', (iter_name,))
        for i in range(m):
            ncfile.createVariable(var_name+str(i), 'f8', (iter_name,))

    # Save initial condition
    if (filepath):
        ncfile.variables[iter_name][0] = t0
        if (is_scalar):
            ncfile.variables[var_name][0] = U[0]
        else:
            for i in range(m):
                ncfile.variables[var_name+str(i)][0] = U[i]

    if (dt > T):
        raise ValueError(f"Time step dt={dt} is larger than total time T={T}. Please choose a smaller dt.")

    n = 0
    t = t0
    while t < T:

        h = min(dt, T - t)
        U1 = U + h * compute_F(F, t, U, is_scalar)

        n += 1
        t += h

        if (filepath):
            ncfile.variables[iter_name][n] = t
            if (is_scalar):
                ncfile.variables[var_name][n] = U1[0]
            else:
                for i in range(m):
                    ncfile.variables[var_name+str(i)][n] = U1[i]

        U = U1

    if (filepath):
        ncfile.close()

    return U
