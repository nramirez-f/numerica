
"""
One-step time integrators for ODEs.
"""

def euler(dt, U, F, t = None):
    """
    Euler method for advancing the solution of an ODE by one time step.
    """
    
    if callable(F):
        if t is None:
            dU_dt = F(U)
        else:
            dU_dt = F(t, U)
    else:
        dU_dt = F
    
    U_new = U + dt * dU_dt
    
    return U_new
