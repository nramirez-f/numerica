import numpy as np
import src.numerica.graph as g
from src.numerica.roots import bisection

def fifth(x):
    return x*x*x*x*x - 5*x*x*x + 1

a  = 0
b  = 1
nx = 1000

x = np.linspace(a,b,nx)
g.plot(fifth,x,title='Quinta')

root = bisection(a,b,fifth,max_iterations=20,debug=True)
print(f'Approximate root found: {root}') 
"""
Note: 
observamos que la solución encontrada cuadra con la gráfica
y que con 20 iteraciones estabilizamos cuatro cifras
"""

""" 
a  = -3
b  = -2
nx = 1000

x = np.linspace(a,b,nx)
g.plot(fifth,x,title='Quinta')

root = bisection(a,b,fifth,max_iterations=20,debug=True)
print(f'Approximate root found: {root}') 
"""
"""
Note: 
observamos que la solución encontrada cuadra con la gráfica
y que con 20 iteraciones estabilizamos seis cifras
"""

""" 
a  = 2
b  = 3
nx = 1000

x = np.linspace(a,b,nx)
g.plot(fifth,x,title='Quinta')

root = bisection(a,b,fifth,max_iterations=20,debug=True)
print(f'Approximate root found: {root}') """

"""
Note: 
observamos que la solución encontrada cuadra con la gráfica
y que con 20 iteraciones estabilizamos seis cifras
"""
