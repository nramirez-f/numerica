from numerica.pde.fvm._fvm_1d import fvm_1d
import numpy as np

def burgers_inviscid_1d(left_boundary,
                        right_boundary,
                        number_of_cells,
                        final_time,
                        save_interval,
                        initial_condition,
                        boundary_condition='periodic',
                        courant_friedrichs_levy_condition = 0.5,
                        logging=False,
                        numerical_scheme='rusanov'):
    """
    Solves the 1D burgers inviscid equation using the finite volume method.
    """
    
    def burgers_inviscid_1d_physical_flux(U):
        return 0.5 * U * U
    
    def lambda_max_function(U):
        return np.abs(U)
    
    
    def courant_function(U) -> float:
        return np.max(np.abs(U))
    
    def burgers_inviscid_1d_numerical_flux(U, flux):
        if numerical_scheme == 'rusanov':
            from numerica.pde.fvm._riemann_solvers import rusanov
            return rusanov(U, flux, lambda_max_function, bc=boundary_condition)
        elif numerical_scheme == 'lax_friedrichs':
            from numerica.pde.fvm._riemann_solvers import lax_friedrichs
            return lax_friedrichs(U, flux, courant_function, bc=boundary_condition)
        else:
            raise ValueError(f"Unsupported numerical scheme: {numerical_scheme}")
    
    fvm_1d( x_min=left_boundary,
            x_max=right_boundary,
            ncx=number_of_cells,
            T=final_time,
            dtSave=save_interval,
            ic=initial_condition,
            cfl=courant_friedrichs_levy_condition,
            lambda_max_function=courant_function,
            physical_flux_function=burgers_inviscid_1d_physical_flux,
            numerical_flux_function=burgers_inviscid_1d_numerical_flux,
            filename='burgers_inviscid_1d.nc',
            title='1D Burgers Inviscid Equation',
            logging=logging,
            description='Finite Volume Method for 1D Burgers Inviscid Equation',
            references='LeVeque, R. J., & Leveque, R. J. (1992). Numerical methods for conservation laws (Vol. 132). Basel: Birkhäuser.')

            
