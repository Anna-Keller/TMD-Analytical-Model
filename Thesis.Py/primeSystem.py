import numpy as np

# Given parameters: main system
m = 1.05     # Mass of the main system, kg
fn = 227.0   # Natural frequency of the main system, Hz
z = 0.0041  # Damping ratio of the main system

# Calculated parameters
wn = 2*np.pi*fn
k = wn**2*m                # Stiffness of the main system, N/m
c = 2*wn*z*m               # Damping coefficient of the main system kg/sec 