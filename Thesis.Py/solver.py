import numpy as np
from scipy.optimize import fsolve
import primeSystem

# given
z1 = primeSystem.z
m1 = primeSystem.m
f1 = primeSystem.fn

# derived
omega = f1*np.pi*2
a = 1 - z1/4
b = 1.35*np.exp(3.2*z1)

# intermediate check 
print("omega = "+str(omega)+", a = "+str(a)+", b = "+str(b))



initial_guess = 0.1

def get_optimal_m2(k2):

    def equation_to_solve(m2):
        print("given k2 = "+str(k2))
        # left hand side
        lhs = (a**(2*b))*(omega**2)/k2

        # right hand side
        rhs = ((1+m2/m1)**(2*b))/m2
        return lhs - rhs
    
    # find such function parameter (m2) that the function returns 0
    solution = fsolve(equation_to_solve, initial_guess)
    print("Optimal TMD mass is: ", solution[0])
    return solution[0]

