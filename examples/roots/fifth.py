import numpy as np
from numerica.roots import bisection
from numerica.plot import function

def fifth(x):
    return x**5 - 5*x**3 + 1


x = np.linspace(-5,5,100)
function(fifth,x,title='$x^5-5x^3+1$',window_title='Fifth example function')

print("\nStudy of the root in the interval [-3,-2]")
print("=" * 80)

x = np.linspace(-3,-2,100)
function(fifth,x,title='$x^5-5x^3+1$',window_title='fifth example on [-3,-2]')

root = bisection(fifth,-3,-2,maxiter=20,debug=True)

print(f'\nApproximate root found: {root}') 

print(f'\nNote:\nWe observe that with 20 iterations we stabilize six decimal digits.')

print("=" * 80)

print("\nStudy of the root in the interval [0,1]")
print("=" * 80)

x = np.linspace(0,1,100)
function(fifth,x,title='$x^5-5x^3+1$',window_title='fifth example on [0,1]')

root = bisection(fifth,0,1,maxiter=20,debug=True)

print(f'\nApproximate root found: {root}') 

print(f'\nNote:\nWe observe that with 20 iterations we stabilize four decimal digits.')

print("=" * 80)



print("\nStudy of the root in the interval [2,3]")
print("=" * 80)

x = np.linspace(2,3,1000)
function(fifth,x,title='$x^5-5x^3+1$',window_title='Fifth example on [2,3]')

root = bisection(fifth,2,3,maxiter=20,debug=True)

print(f'\nApproximate root found: {root}')

print(f'\nNote:\nWe observe that with 20 iterations we stabilize five decimal digits.')

print("=" * 80)
