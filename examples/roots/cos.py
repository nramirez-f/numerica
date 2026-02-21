import numpy as np
from numerica.roots import bisection
from numerica.roots import regula_falsi
from numerica.plot import function

def cos(x):
    return np.cos(x) - x

a = 0.0
b = 3.0

x = np.linspace(a,b,100)
function(cos,x,title='$cos(x)-x$',window_title=f'Cosine example on [{a},{b}]')

print(f"\nStudy of the root in the interval [{a},{b}] with Bisection method")
print("=" * 80)

root = bisection(cos,a,b,tol=1e-7,debug=True)

print(f'\nApproximate root found: {root}')

print(f'\nNote:\nWe observe that with 24 iterations we stabilize six decimal digits.')

print(f"\nStudy of the root in the interval [{a},{b}] with Regula Falsi method")
print("=" * 80)

root = regula_falsi(cos,a,b,tol=1e-7,debug=True)

print(f'\nApproximate root found: {root}')

print(f'\nNote:\nWe observe that Regula Falsi converges four times faster than Bisection')