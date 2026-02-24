import sys

def secant(f, x0, x1, tol=1e-12, maxiter = 1000, debug=False, stop_criteria='value', display_precision=8):

    if (f(x0)*f(x1) > 0.0):
        raise ValueError(f"No sign change: f(x0)={f(x0):.{display_precision}e} and f(x1)={f(x1):.{display_precision}e} have the same sign. Method cannot be applied.")

    if (debug):
        print(f"{'Iter':>5} | {'left_extreme':>15} | {'right_extreme':>15} | {'approx_root':>15} | {'value':>15}")
        print("-" * 80)
    
    n = 1
    while (n < (maxiter + 1)):
        try:
            if (f(x1) == f(x0)):
                raise ValueError(f"Function values at the extremes are equal: f(x0{n})={f(x0):.{display_precision}e} and f(x1{n})={f(x1):.{display_precision}e}. Method cannot be applied.")
            else:
                x_new = x1 - f(x1)*(x1-x0)/(f(x1) - f(x0))

            if (debug):
                print(f"{n:>5} | {x0:>15.{display_precision}e} | {x1:>15.{display_precision}e} | {x_new:>15.{display_precision}e} | {f(x_new):>15.{display_precision}e}")

            if (abs(f(x_new)) < sys.float_info.epsilon):
                if (debug):
                    print(f"\nRoot found at x = {x_new:.{display_precision}e}")
                return x_new
            else:
                x0 = x1
                x1 = x_new

            if (stop_criteria == 'heuristic' and abs(x1-x0) < tol or
                stop_criteria == 'value' and abs(f(x1)) < tol):
                
                if (debug):
                    print('-' * 80)
                    print(f"\nConvergence by {stop_criteria} criteria achieved. Approx root at x = {x_new:.{display_precision}e} with value = {f(x_new):.{display_precision}e}")
                return x_new
            
            n += 1
        except ValueError as e:
            print(f"\nError at iteration {n}: {e}")
            raise

    if (debug):
        print('-' * 80)
        print(f'\nMaximum iterations reached. Approximate root at x = {x_new:.{display_precision}e} with value = {f(x_new):.{display_precision}e}')
    
    return x_new