import numpy as np

def bisection(f, a, b, tol=1e-12, maxiter = 100, debug=False, display_precision=8):

    if (f(a)*f(b) > 0.0):
        raise ValueError(f"No sign change: f(a)={f(a):.{display_precision}e} and f(b)={f(b):.{display_precision}e} have the same sign. Bisection method cannot be applied.")

    if (debug):
        print(f"{'Iter':>5} | {'left_extreme':>15} | {'right_extreme':>15} | {'approx_root':>15} | {'value':>15}")
        print("-" * 80)

    # Max iterations depending on tolerance
    maxiter_tol = int((np.log(b-a) - np.log(tol))/np.log(2) - 1) + 1

    N = min(maxiter, maxiter_tol)

    n = 1
    while (n < (N + 1)):
        
        approx_root = 0.5 * (a + b)

        if (debug):
            print(f"{n:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {approx_root:>15.{display_precision}e} | {f(approx_root):>15.{display_precision}e}")

        if (f(a) * f(approx_root) < 0.0):
            b = approx_root
        else:
            a = approx_root
        
        n += 1

    if (debug):
        print('-' * 80)
        print(f'\nApproximate root found at x = {approx_root:.{display_precision}e} with value = {f(approx_root):.{display_precision}e}')

    return approx_root