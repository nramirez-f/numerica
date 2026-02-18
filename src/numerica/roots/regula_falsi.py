
def regula_falsi(f, a, b, tol=1e-12, maxiter = 1000, debug=False, display_precision=8):

    if (debug):
        print(f"{'Iter':>5} | {'a_n':>15} | {'b_n':>15} | {'root':>15} | {'f(root)':>15}")
        print("-" * 80)

    n = 0
    while (n < (maxiter + 1)):
        
        c = b - f(b)*(b-a)/(f(b) - f(a))

        if (f(a)*f(c) < 0.0):
            b = c
        else:
            a = c

        if (debug):
            print(f"{n:>5} | {a:>15.{display_precision}e} | {b:>15.{display_precision}e} | {c:>15.{display_precision}e} | {f(c):>15.{display_precision}e}")

        if (abs(f(c)) < tol):
            if (debug):
                print(f'\nFound root with tol {tol:.{display_precision}e} at x = {c:.{display_precision}e} with f(x) = {f(c):.{display_precision}e}')
            return c
        
        n += 1

    if (debug):
        print('-' * 80)
        print(f'\nMaximum iterations reached. Approximate root at x = {c:.{display_precision}e} with f(x) = {f(c):.{display_precision}e}')
    
    return c
