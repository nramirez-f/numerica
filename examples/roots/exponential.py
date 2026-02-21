import numpy as np
from numerica.roots import bisection
from numerica.roots import regula_falsi
from numerica.plot import function

def exponential(x):
    return x - np.exp(-x)

x = np.linspace(-1.0,2.0,100)
function(exponential,x,title='$x-e^{-x}$',window_title='Exponential example on [-1,2]')

print ("Finding root of x - exp(-x) on [0,1] with bisection method and tol = 0.5e-6")
bisection(exponential,0,1,tol=0.5*1e-6,debug=True)

print ("\nFinding root of x - exp(-x) on [0,1] with regula falsi method and tol = 0.5e-6")
regula_falsi(exponential,0,1,tol=0.5*1e-6,debug=True,stop_criteria='interval')
