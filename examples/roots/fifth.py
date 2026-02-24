import numpy as np
from numerica.roots import bisection, regula_falsi, secant
from numerica.plot import function

def fifth(x):
    return x**5 - 5*x**3 + 1

print("=" * 80)
print("Problem: Find the roots of f(x) = x^5 - 5x^3 + 1")
print("\nMethod: We will use the methods of bisection, regula falsi")
print("and secant to approximate the roots in a interval [a,b] where sign changes occur.")
print("=" * 80)

x = np.linspace(-2.5,2.5,100)
function(fifth,x,title='$f(x) = x^5-5x^3+1$',window_title='Fifth example function')

a = float(input("\nEnter the left extreme of the interval (a): "))
b = float(input("Enter the right extreme of the interval (b): "))

print(f"\nStudy of the root in the interval [{a},{b}]")
print("=" * 80)

print('\n# Bisection\n')

bisection(fifth,a,b,tol=1e-7,debug=True)

print('\n# Regula Falsi (Heuristic)\n')

regula_falsi(fifth,a,b,tol=1e-7,stop_criteria='heuristic',debug=True)

print('\n# Regula Falsi (Value)\n')

regula_falsi(fifth,a,b,tol=1e-7,stop_criteria='value',debug=True)

print('\n# Secant (Heuristic)\n')

secant(fifth,a,b,tol=1e-7,stop_criteria='heuristic',debug=True)

print('\n# Secant (Value)\n')

secant(fifth,a,b,tol=1e-7,stop_criteria='value',debug=True)

print("=" * 80)

x = np.linspace(a,b,100)
function(fifth,x,title='$f(x) = x^5-5x^3+1$',window_title=f'fifth example on [{a},{b}]')
    