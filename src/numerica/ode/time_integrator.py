
"""
One-step time integrators for ODEs.
"""

def _euler(dt, U0, F, t = None):
    """
    Euler method for advancing the solution of an ODE by one time step.
    """
    
    if callable(F):
        if t is None:
            F0 = F(U0)
        else:
            F0 = F(t, U0)
    else:
        F0 = F
    
    U1 = U0 + dt * F0
    
    return U1



