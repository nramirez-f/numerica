import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import os
from numerica.ode import euler

def f1(t,U):
    return 0.25*U[0] - 0.01*U[0]*U[1]

def f2(t,U):
    return -0.5*U[1] + 0.01*U[0]*U[1]

def F(t,U):
    return np.array([f1(t,U), f2(t,U)])

# Initial conditions
t0 = 0.0 # Initial time
T = 20.0 # Final time
dt = 0.1 # Time step
U0 = np.array([80.0, 30.0]) # Initial conditions: [Prey population, Predator population]

# Time integration for ODE system
euler(F, t0, U0, T, dt, filepath='lotka_volterra.nc')

# Plotting results
file = nc.Dataset('lotka_volterra.nc', 'r')
time = file.variables['t'][:]
prey = file.variables['u0'][:]
predator = file.variables['u1'][:]
file.close()

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
ax_prey = axes[0, 0]
ax_pred = axes[0, 1]
ax_phase = axes[1, :]

# Prey
ax_prey.plot(time, prey, color='tab:blue', marker='o', markersize=2)
ax_prey.set_title('Preys')
ax_prey.set_xlabel('time')
ax_prey.set_ylabel('Population')
ax_prey.grid(True)

# Predators
ax_pred.plot(time, predator, color='tab:orange', marker='o', markersize=2)
ax_pred.set_title('Predators')
ax_pred.set_xlabel('time')
ax_pred.set_ylabel('Population')
ax_pred.grid(True)

# Phase diagram — remove the two individual axes and replace with a wide one
for ax in axes[1, :]:
    ax.remove()
ax_phase = fig.add_subplot(2, 1, 2)
ax_phase.plot(prey, predator, color='tab:green', linewidth=0.8)

# Directional arrows along the trajectory
n_arrows = 12
arrow_indices = np.linspace(0, len(prey) - 2, n_arrows, dtype=int)
for i in arrow_indices:
    ax_phase.annotate('',
        xy=(prey[i+1], predator[i+1]),
        xytext=(prey[i], predator[i]),
        arrowprops=dict(arrowstyle='->', color='tab:green', lw=1.5))

ax_phase.scatter(prey[0], predator[0], color='green', zorder=5, label='Init')
ax_phase.scatter(prey[-1], predator[-1], color='red', zorder=5, label='Final')
ax_phase.set_title('Phase Diagram')
ax_phase.set_xlabel('Preys')
ax_phase.set_ylabel('Predators')
ax_phase.legend()
ax_phase.grid(True)

plt.tight_layout()
plt.show()

if os.path.exists('lotka_volterra.nc'):
        os.remove('lotka_volterra.nc')
