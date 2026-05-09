from numerica.pde.fvm._fvm_1d import fvm_1d

def advection_1d(left_boundary,
                 right_boundary,
                 number_of_cells,
                 final_time,
                 save_interval,
                 initial_condition,
                 velocity,
                 boundary_condition='periodic',
                 courant_friedrichs_levy_condition = 0.5,
                 logging=False):
    """
    Solves the 1D advection equation using the finite volume method.
    """
    
    def advection_1d_physical_flux(U):
        return velocity * U
    
    def advection_1d_numerical_flux(U, flux):
        from numerica.pde.fvm._riemann_solvers import upwind
        return upwind(U, flux, velocity, bc=boundary_condition)
    
    def courant_function(U):
        return abs(velocity)
    
    fvm_1d( x_min=left_boundary,
            x_max=right_boundary,
            ncx=number_of_cells,
            T=final_time,
            dtSave=save_interval,
            ic=initial_condition,
            cfl=courant_friedrichs_levy_condition,
            lambda_max_function=courant_function,
            physical_flux_function=advection_1d_physical_flux,
            numerical_flux_function=advection_1d_numerical_flux,
            filename='advection_1d.nc',
            title='1D Advection Equation',
            logging=logging,
            description='Finite Volume Method for 1D Advection Equation',
            references='LeVeque, R. J., & Leveque, R. J. (1992). Numerical methods for conservation laws (Vol. 132). Basel: Birkhäuser.')

            
