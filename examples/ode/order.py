import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
from numerica.ode import euler, heun, taylor, heun, rk4
import pandas as pd
import os

from numerica.ode import euler

def exact_solution(t):
    return t**2 - 4.0*t + 8.0 - 7.0 * np.exp(-0.5*t)

fig, ax = plt.subplots()
t = np.linspace(0, 10, 100)
plt.plot(t, exact_solution(t), label='Exact Solution', linestyle='solid', color='black')

def f(t,u):
    return 0.5*(t**2-u)

# Temporal derivatives
def df(t,u):
    return t - 0.5 * f(t,u)

def df2(t,u):
    return 1.0 - 0.5 * df(t,u)

refination_factor = 2
samples = 4
dt_list = [0.5 / (refination_factor**i) for i in range(samples)]

Method = 'Approximate Solution'
time_integrator = euler

# Plotting Approx solutions
for dt in dt_list:    

    time_integrator(f, 0.0, 1.0, 10.0, dt, filepath=f'approx_solution_{dt}.nc')

    file = nc.Dataset(f'approx_solution_{dt}.nc', 'r')

    time = file.variables['t'][:]
    u = file.variables['u'][:]
    plt.plot(time, u, label=f'{Method} (dt={dt})', marker='o', markersize=2)

    file.close()

plt.title(f'Approximate Solutions using {Method} Method')
plt.xlabel('t(s)')
plt.ylabel('u(t)')
plt.legend()
plt.show()

# Error analysis
errors_list = []

for dt in dt_list:    
    file = nc.Dataset(f'approx_solution_{dt}.nc', 'r')
    time = file.variables['t'][:]
    u = file.variables['u'][:]
    exact_u = exact_solution(time)
    error = np.abs(u - exact_u)
    file.close()
    errors_list.append(error[-1])

error_data = {
    'dt': dt_list,
    'Error(Linf)': errors_list,
    'Quotient': ['-'] + [errors_list[i-1] / errors_list[i] for i in range(1, len(errors_list))],
    'Order': ['-'] + [np.log(errors_list[i-1] / errors_list[i]) / np.log(refination_factor) for i in range(1, len(errors_list))]
}

df = pd.DataFrame(error_data)
print(f"\nOrder Table (Refinement Factor = {refination_factor}):")
print(df.to_string(index=False))

for dt in dt_list:
    filename = f'approx_solution_{dt}.nc'
    if os.path.exists(filename):
        os.remove(filename)
