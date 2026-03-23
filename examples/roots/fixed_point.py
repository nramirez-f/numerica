from numerica.roots import fixed_point, alpha_method, newton_method
import matplotlib.pyplot as plt
import numpy as np

def print_successive_approximations(f, succ):

    print(f"{'Iteration':>10} | {'x':>18} | {'f(x)':>18} | {'|x_n - x_{n-1}|':>18}")
    print("-" * 80)
    for n, x in enumerate(succ):
        diff = abs(succ[n] - succ[n-1]) if n > 0 else 0.0
        print(f"{n:>10} | {x:>18.10e} | {f(x):>18.10e} | {diff:>18.10e}")
    print("-" * 80)
    
print('Exercise 1: Fixed-point iteration for f(x) = x - exp(-x)')
print(80 * '=')

def f1(x):
    return x - np.exp(-x)

def g1(x):
    return np.exp(-x)

def g1_newton(x):
    return x - (x - np.exp(-x)) / (1 + np.exp(-x))

x0 = 0.5
tolerance = 1e-7
max_iterations = 100

print('Using g(x) = exp(-x):\n')
succession1 = []
fixed_point(g1, x0, tol=tolerance, max_iter=max_iterations, x_values=succession1)
print_successive_approximations(f1, succession1)

print('Using Newton\'s method:\n')
succession1_newton = []
fixed_point(g1_newton, x0, tol=tolerance, max_iter=max_iterations, x_values=succession1_newton)
print_successive_approximations(f1, succession1_newton)

print(80 * '=')

print('Exercise 2: Fixed-point of Kepler\'s equation K = x - alpha * sin(x)')
print(80 * '=')

K = 2.0 / 3.0
alpha = 0.093
x0 = 0.5
tolerance = 1e-7
max_iterations = 100

def f2(x):
    return x - (K + alpha * np.sin(x))

def g2(x):
    return K + alpha * np.sin(x)

print('Using g(x) = K + alpha * sin(x):\n')
succession2 = []
fixed_point(g2, x0, tol=tolerance, max_iter=max_iterations, x_values=succession2)
print_successive_approximations(f2, succession2)

print('Using Newton\'s method:\n')
def g2_newton(x):
    return x - (x - (K + alpha * np.sin(x))) / (1 - alpha * np.cos(x))

succession2_newton = []
fixed_point(g2_newton, x0, tol=tolerance, max_iter=max_iterations, x_values=succession2_newton)
print_successive_approximations(f2, succession2_newton)

print(80 * '=')

print('Exercise 3: Fixed-point iteration for f(x) = cos(x) - x')
print(80 * '=')

def f3(x):  
    return np.cos(x) - x

def g3(x):
    return np.cos(x)

def g3_newton(x):
    return x - (np.cos(x) - x) / (-np.sin(x) - 1.0)

x0 = 0.5
tolerance = 1e-7
max_iterations = 100

print('Using g(x) = cos(x):\n')
succession3 = []
fixed_point(g3, x0, tol=tolerance, max_iter=max_iterations, x_values=succession3)
print_successive_approximations(f3, succession3)

print('Using Newton\'s method:\n')
succession3_newton = []
fixed_point(g3_newton, x0, tol=tolerance, max_iter=max_iterations, x_values=succession3_newton)
print_successive_approximations(f3, succession3_newton)

print(80 * '=')

print('Exercise 4: Fixed-point iteration for f(x) = x^5 - 5*x^3 + 1')

def f4(x):
    return x**5 - 5*x**3 + 1

def g4_newton(x):
    return x - (x**5 - 5*x**3 + 1) / (5*x**4 - 15*x**2)

x0 = 0.5
tolerance = 1e-7
max_iterations = 100

print('Using Newton\'s method:\n')

succession4_newton = []
fixed_point(g4_newton, x0, tol=tolerance, max_iter=max_iterations, x_values=succession4_newton)
print_successive_approximations(f4, succession4_newton)



alpha4 = -0.12
print(f'Using alpha method with alpha = {alpha4}:\n')

def g4(x):
    return x - alpha4 * f4(x)

def dg4(x):
    return 1 - alpha4 * (5*x**4 - 15*x**2)

x4 = np.linspace(0.0, 1.0, 400)

fig, ax = plt.subplots()

ax.plot(x4, g4(x4), label='g', color='blue')
ax.plot(x4, dg4(x4), label='dg', color='green')
ax.plot(x4, x4, label='y = x', color='red', linestyle='--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Exercise 4: Alpha method (alpha = {alpha4})')
ax.legend()

plt.show()

succession4_alpha = []
alpha_method(alpha4, f4, x0, tol=tolerance, max_iter=max_iterations, x_values=succession4_alpha)
print_successive_approximations(f4, succession4_alpha)

print (80 * '=')

print('Exercise 5: Fixed-point iteration for f(x) = x + (x - 1) * exp(x)')

def f5(x):
    return x + (x - 1) * np.exp(x)

def df5(x):
    return 1.0 + x * np.exp(x)

x5 = np.linspace(0.0, 1.0, 400)
fig, ax = plt.subplots()
ax.plot(x5, f5(x5), label='f', color='blue')
ax.set_title('Exercise 5: f(x) = x + (x - 1) * exp(x)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid()
plt.show()

x0 = 0.65
tolerance = 1e-8
max_iterations = 100

print('Using Newton\'s method:\n')

succession5_newton = []
r5 = newton_method(f5, df5, x0, tol=tolerance, max_iter=max_iterations, x_values=succession5_newton)
print_successive_approximations(f5, succession5_newton)

alpha5 = 0.5
print(f'Using alpha method with alpha = {alpha5}:\n')

succession5_alpha = []
alpha_method(alpha5, f5, x0, tol=tolerance, max_iter=max_iterations, x_values=succession5_alpha)
print_successive_approximations(f5, succession5_alpha)

print('Using fixed-point iteration with g(x) = -(x - 1) * exp(x):\n')

def g5(x):
    return -(x - 1) * np.exp(x)

def dg5(x):
    return -(x *np.exp(x))

succession5_fixed_point = []
fixed_point(g5, x0, tol=tolerance, max_iter=max_iterations, x_values=succession5_fixed_point)

print(f'This method does not converge because |g\'(r)| = {abs(dg5(r5))} >= 1, where r is the root we are trying to find.'.format(abs(dg5(r5))))

print (80 * '=')
