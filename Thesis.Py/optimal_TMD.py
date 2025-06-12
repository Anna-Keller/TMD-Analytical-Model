import numpy as np
import math
import solver


def get_TMD_parameters_DenHartog(mu_values, m1, wn1):
    TMD_parameters = []
    for mu in mu_values:
        mu = round(mu, 2)
        m2 = mu * m1
        f_opt = 1 / (1 + mu)
        wn2 = f_opt * wn1
        k2 = wn2**2 * m2
        z2 = np.sqrt(3 * mu / (8 * (1 + mu)))
        c2 = 2 * m2 * wn2 * z2
        TMD_parameters.append((m2, c2, k2, z2, mu))
    return TMD_parameters


def get_TMD_parameters_Lin(mu_values, m1, wn1, z1):
    TMD_parameters = []
    for mu in mu_values:
        mu = round(mu, 2)
        m2 = mu * m1
        a = 1 - z1/4
        b = 1.35 * math.exp(3.2*z1)
        f_opt = (a / (1 + mu))**b
        wn2 = f_opt * wn1
        k2 = wn2**2 * m2
        z2 = 0.46* mu**0.48
        c2 = 2 * m2 * wn2 * z2
        TMD_parameters.append((m2, c2, k2, z2, mu))
    return TMD_parameters

def solve_quadratic(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 and returns the solutions."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None  # No real solutions
    else:
        # Calculate both solutions using the quadratic formula
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2

def get_TMD_parameters_by_k_denHartog(k2, wn1, m1, z2):
    # Coefficients for the quadratic equation
    a = k2
    b = 2 * k2 * m1 - m1**2 * wn1**2
    c = k2 * m1**2
    
    # Solving the quadratic equation
    m2_1, m2_2 = solve_quadratic(a, b, c)
    TMD_parameters = []
    for m2 in [m2_1, m2_2]:
        if m2 is not None:
            mu = m2 / m1
            c2 = 2 * m2 * wn1 * z2  # Calculating damping coefficient for TMD
            TMD_parameters.append((m2, c2, k2, mu, z2))
    return TMD_parameters

def get_TMD_parameters_by_k_Lin(k2, wn1, m1, z2): 
    TMD_parameters = []
    m2 = solver.get_optimal_m2(k2)
    mu = m2/m1
    c2 = 2 * m2 * wn1 * z2

    TMD_parameters.append((m2, c2, k2, mu, z2))
    return TMD_parameters