

def iteration(f, a, b):

    c = b - f(b)*(b-a)/(f(b) - f(a))

    if (f(a)*f(c) < 0.0):
        b = c
    else:
        a = c

    return c, a, b

def regula_falsi(f, a, b, tol=1e-12, maxiter = 1000, debug=False, display_precision=8):

    if (debug):
        print(f"{'Iter':>5} | {'a_n':>15} | {'b_n':>15} | {'root':>15} | {'f(root)':>15}")
        print("-" * 80)

    c0, a, b = iteration(f, a, b)
    if (debug):
        print(f"{0:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {c0:>15.{display_precision}e} | {f(c0):>15.{display_precision}e}")

    n = 1
    iter_diff = 1.0
    while (n < (maxiter + 1)):
        
        c1, a, b = iteration(f, a, b)
        if (debug):
            print(f"{n:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {c1:>15.{display_precision}e} | {f(c1):>15.{display_precision}e}")

        iter_diff = abs(c1 - c0)

        if (iter_diff < tol):
            if (debug):
                print(f'\nFound root with tol {tol:.{display_precision}e} at x = {c1:.{display_precision}e} with f(x) = {f(c1):.{display_precision}e}')
            return c1
        
        c0 = c1
        n += 1

    if (debug):
        print('-' * 80)
        if (n >= maxiter):
            print(f'\nMaximum iterations reached. Approximate root at x = {c1:.{display_precision}e} with f(x) = {f(c1):.{display_precision}e}')
        else:
            print(f'\nTolerance reached. Approximate root at x = {c1:.{display_precision}e} with f(x) = {f(c1):.{display_precision}e}')
    
    return c1