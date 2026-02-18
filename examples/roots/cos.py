import numpy as np
from numerica.roots import bisection
from numerica.plot import function

def cosine(x):
    return np.cos(x) - x

a = 0.0
b = 3.0


print(f"\nStudy of the root in the interval [{a},{b}]")
print("=" * 80)
x = np.linspace(a,b,100)
function(cosine,x,title='$cos(x)-x$',window_title=f'Cosine example on [{a},{b}]')

root = bisection(a,b,cosine,tol=1e-7,debug=True)

print(f'\nNote:\nWe observe that with 20 iterations we stabilize five decimal digits.')

print(f'\nApproximate root found: {root}')

