import numpy as np

def riemannStates(U, bc):

    noi = len(U) + 1 # number of intercells
    
    # Intercell indexes
    ic_idexes = np.arange(noi)
    iL = ic_idexes - 1
    iR = ic_idexes

    if bc == 'periodic':
        iL[0]  = len(U) - 1
        iR[-1] = 0
    if bc == 'open':
        iL[0]  = 0
        iR[-1] = len(U) - 1

    UL_star, UR_star = U[iL], U[iR]

    return UL_star, UR_star

def upwind(U, phisical_flux, upwind_term, bc='periodic'):
    """Upwind Riemann solver"""

    F_star = np.zeros(len(U) + 1)

    UL, UR = riemannStates(U, bc)
    
    if upwind_term > 0:
        F_star = phisical_flux(UL)
    else:
        F_star = phisical_flux(UR)

    return F_star

def lax_friedrichs(U, phisical_flux, courant_function, bc):
    """Lax-Friedrichs Riemann solver"""

    F_star = np.zeros(len(U) + 1)

    UL, UR = riemannStates(U, bc)

    max_wave_speed: float = courant_function(U)

    F_star = 0.5 * (phisical_flux(UL) + phisical_flux(UR)) - 0.5 * max_wave_speed * (UR - UL)

    return F_star

def rusanov(U, phisical_flux, lambda_max_function, bc):
    """Rusanov (local Lax-Friedrichs) Riemann solver"""

    F_star = np.zeros(len(U) + 1)

    UL, UR = riemannStates(U, bc)

    local_max_wave_speed: np.ndarray = np.maximum(lambda_max_function(UL), lambda_max_function(UR))

    F_star = 0.5 * (phisical_flux(UL) + phisical_flux(UR)) - 0.5 * local_max_wave_speed * (UR - UL)

    return F_star