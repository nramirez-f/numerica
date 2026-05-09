
"""
One-step time integrators for ODEs.
"""

def euler(dt, U, F, t = None):
    """
    Euler method for advancing the solution of an ODE by one time step.
    """

    if (t is None):
        U_new = U + dt * F(U)
    else:
        U_new = U + dt * F(t, U)

    return U_new
