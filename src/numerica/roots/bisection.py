import numpy as np

def bisection(f, a, b, tol=1e-12, maxiter = 0, debug=False, display_precision=8):

    if (debug):
        print(f"{'Iter':>5} | {'a_n':>15} | {'b_n':>15} | {'root':>15} | {'f(root)':>15}")
        print("-" * 80)

    maxiter_tol = int((np.log(b-a) - np.log(tol))/np.log(2)) + 1 # Max iterations depending on tolerance

    if (maxiter > 0):
        itermax = min(maxiter, maxiter_tol)
    else:
        itermax = maxiter_tol

    n = 0
    while (n < (itermax + 1)):
        
        approx_root = 0.5*(a + b)

        if (debug):
            print(f"{n:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {approx_root:>15.{display_precision}e} | {f(approx_root):>15.{display_precision}e}")
        if (abs(f(approx_root)) < tol):
            if (debug):
                print(f'\nFound root with tol {tol:.{display_precision}e} at x = {approx_root:.{display_precision}e} with f(x) = {f(approx_root):.{display_precision}e}')
            return approx_root
        else:
            if (f(a)*f(approx_root) < 0.0):
                b = approx_root
            else:
                a = approx_root
        
        n += 1

    if (debug):
        print('-' * 80)
        print(f'\nMaximum iterations reached. Approximate root at x = {approx_root:.{display_precision}e} with f(x) = {f(approx_root):.{display_precision}e}')

    return approx_root