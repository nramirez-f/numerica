import netCDF4 as nc
import time

def heun(f,t0,u0,T,dt,
          filepath=None,iter_name='t',iter_unit='s',var_name='u'):

    if (filepath):
        ncfile = nc.Dataset(filepath, 'w', format='NETCDF4')
        ncfile.history = 'Created at ' + time.ctime(time.time())
        ncfile.source = 'Numerica Library'
        ncfile.description = 'Heun method for ODE integration'
        ncfile.createDimension(iter_name, None)
        ncfile.createVariable(iter_name, 'f8', (iter_name,)).units = iter_unit
        ncfile.createVariable(var_name, 'f8', (iter_name))


    # Save initial condition
    if (filepath):
        ncfile.variables[iter_name][0] = t0
        ncfile.variables[var_name][0] = u0

    if (dt > T):
        raise ValueError(f"Time step dt={dt} is larger than total time T={T}. Please choose a smaller dt.")
    
    u = u0
    n = 0
    t = t0
    while t < T:

        u_1 = u + dt * f(t, u)
        u1 = u + 0.5 * dt * (f(t, u) + f(t + dt, u_1))

        n += 1
        t += min(dt, T - t)
        
        if (filepath):
            ncfile.variables[iter_name][n] = t
            ncfile.variables[var_name][n]  = u1

        u = u1
       
    if (filepath):
        ncfile.close()
