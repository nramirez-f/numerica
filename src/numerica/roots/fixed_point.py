
import math

def fixed_point(g, x0, tol=1e-8, max_iter=1000, x_values=None):
    
    x = x0

    if x_values is not None:
        x_values.append(x)
    
    n = 0
    while n < max_iter:

        x_new = g(x)

        if math.isnan(x_new) or math.isinf(x_new):
            raise ValueError(f"Error occurred while evaluating g(x) at iteration {n+1}, g({x:.15e}) = {x_new:.15e}")
        
        if x_values is not None:
            x_values.append(x_new)

        if g(x_new) == x_new:
            print(f"Exact fixed point found at iteration {n+1}: x = {x_new:.15e}")
            return x_new
        elif abs(x_new - x) < tol:
            print(f"Convergence criteria achieved at iteration {n+1}: x = {x_new:.15e}, |g(x) - x| = {abs(x_new - x):.2e}")
            return x_new
        
        x = x_new
        n += 1
    
    print(f"Warning: fixed-point iteration did not converge after {max_iter} iterations.")

    return x


def alpha_method(alpha, f, x0, tol=1e-8, max_iter=1000, x_values=None):
    def g(x):
        return x - alpha * f(x)
    
    return fixed_point(g, x0, tol=tol, max_iter=max_iter, x_values=x_values)

def newton_method(f, df, x0, tol=1e-8, max_iter=1000, x_values=None):
    def g(x):
        if df(x) == 0:
            raise ValueError(f"Derivative is zero at x = {x:.15e}, cannot perform Newton's method.")
        else:
            return x - f(x) / df(x)
    
    return fixed_point(g, x0, tol=tol, max_iter=max_iter, x_values=x_values)