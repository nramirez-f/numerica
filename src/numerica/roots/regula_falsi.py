import sys

def regula_falsi(f, a, b, tol=1e-12, maxiter = 1000, debug=False, stop_criteria='value', display_precision=8):

    if (f(a)*f(b) > 0.0):
        raise ValueError(f"No sign change: f(a)={f(a):.{display_precision}e} and f(b)={f(b):.{display_precision}e} have the same sign. Method cannot be applied.")

    if (debug):
        print(f"{'Iter':>5} | {'left_extreme':>15} | {'right_extreme':>15} | {'approx_root':>15} | {'value':>15}")
        print("-" * 80)

    n = 1
    c_old = a
    while (n < (maxiter + 1)):
        
        if (f(b) == f(a)):
            raise ValueError(f"Function values at the extremes are equal: f(a{n})={f(a):.{display_precision}e} and f(b{n})={f(b):.{display_precision}e}. Method cannot be applied.")
        else:
            c = b - f(b)*(b-a)/(f(b) - f(a))

        if (debug):
            print(f"{n:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {c:>15.{display_precision}e} | {f(c):>15.{display_precision}e}")

        if (abs(f(c)) < sys.float_info.epsilon):
            if (debug):
                print(f"\nRoot found at x = {c:.{display_precision}e}")
            return c
        
        elif (f(a)*f(c) < 0.0):
            b = c

        else:
            a = c

        if (stop_criteria == 'interval' and abs(b-a) < tol or
            stop_criteria == 'heuristic' and abs(c - c_old) < tol or
            stop_criteria == 'value' and abs(f(c)) < tol):
            
            if (debug):
                print('-' * 80)
                print(f"\nConvergence criteria achieved. Approx root at x = {c:.{display_precision}e} with value = {f(c):.{display_precision}e}")
            return c
        
        c_old = c
        n += 1

    if (debug):
        print('-' * 80)
        print(f'\nMaximum iterations reached. Approximate root at x = {c:.{display_precision}e} with value = {f(c):.{display_precision}e}')
    
    return c
