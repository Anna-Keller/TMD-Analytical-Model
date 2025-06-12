import numpy as np
import matplotlib.pyplot as plt
import primeSystem
import optimal_TMD
import frf

m1 = primeSystem.m   # Mass of the main system, kg
wn1 = primeSystem.wn # Angular natural frequency of the main system, rad/sec
c1 = primeSystem.c   # Damping coefficient of the main system
k1 = primeSystem.k   # Stiffness of the main system, N/m
z1 = primeSystem.z   # Damping ratio of the main system

# Range of frequencies to analyze
freq_range = np.linspace(100, 600, 300) # Range of frequencies

# Primary system FRF calculated
untuned_FRF_calc = frf.untuned_FRF(freq_range, m1, c1, k1)

# Get optimal TMD parameters for each mu value (Den Hartog)
mu_values = np.linspace(0.01, 0.2, 20)
TMD_parameters_DenHartog = optimal_TMD.get_TMD_parameters_DenHartog(mu_values, m1, wn1)

# Get optimal TMD parameters for each mu value (Lin)
TMD_parameters_Lin = optimal_TMD.get_TMD_parameters_Lin(mu_values, m1, wn1, z1) 

# Optimal TMD with fixed k2
fixed_k2 = 168000
fixed_z2 = 0.07
TMD_parameters_by_k_denHartog = optimal_TMD.get_TMD_parameters_by_k_denHartog(fixed_k2, wn1, m1, fixed_z2)
TMD_parameters_by_k_Lin = optimal_TMD.get_TMD_parameters_by_k_Lin(fixed_k2, wn1, m1, fixed_z2)

# Create a 1x2 grid of subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))  # Adjust the figure size as needed

# First Graph
plt.sca(axes[0])  # Select the first subplot

plt.plot(np.abs(freq_range), np.abs(untuned_FRF_calc), label='System without TMD', color='orange')
#plt.plot(np.abs(freq_range), tuned_FRF_Calc, label='System with TMD', color='black')
for m2, c2, k2, z2, mu in TMD_parameters_DenHartog:
    tuned_FRF_range = frf.tuned_FRF(freq_range, m1, c1, k1, m2, c2, k2)
    axes[0].plot(np.abs(freq_range), tuned_FRF_range, label=f"mu = {mu}, k2 = {k2:.2f}, m2 = {m2:.2f}, z2 = {z2:.2f}")
    plt.plot(np.abs(freq_range), tuned_FRF_range)
axes[0].set_title("Optimal TMD (Den Hartog)")
axes[0].set_xlabel('Frequency, Hz')
axes[0].set_ylabel('Amplitude, m/s^2/N')
axes[0].legend()
axes[0].grid()

# Second Graph
plt.sca(axes[1])  # Select the second subplot
plt.plot(np.abs(freq_range), np.abs(untuned_FRF_calc), label='System without TMD', color='orange')
for m2, c2, k2, z2, mu in TMD_parameters_Lin:
    tuned_FRF_range = frf.tuned_FRF(freq_range, m1, c1, k1, m2, c2, k2)
    plt.plot(np.abs(freq_range), tuned_FRF_range, label=f"mu = {mu}, k2 = {k2:.2f}, m2 = {m2:.2f}, z2 = {z2:.2f}")
    #plt.plot(np.abs(freq_range), tuned_FRF_range)
axes[1].set_title("Optimal TMD (Lin)")
axes[1].set_xlabel('Frequency, Hz')
axes[1].set_ylabel('Amplitude, m/s^2/N')
axes[1].legend()
axes[1].grid()

# Adjust spacing between subplots
plt.tight_layout()

# Setting up the plot for Figures 3 & 4
# Create a 1x2 grid of subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))  

# First Graph
plt.sca(axes[0])  # Select the first subplot

plt.plot(np.abs(freq_range), np.abs(untuned_FRF_calc), label='System without TMD', color='orange')

# Different colors for each TMD configuration for clarity
colors = ['blue', 'green', 'red', 'purple', 'brown', 'black']
color_index = 0

for m2, c2, k2, mu, z2 in TMD_parameters_by_k_denHartog:
    if m2 is not None:  # Ensure m2 was calculated successfully
        tuned_FRF_range = frf.tuned_FRF(freq_range, m1, c1, k1, m2, c2, k2)
        plt.plot(np.abs(freq_range), tuned_FRF_range, 
                 label=f"mu = {mu:.2f}, k2 = {k2:.0f}, m2 = {m2:.6f}, z2 = {z2:.2f}",  # Display mu, k2, m2, z2 in legend
                 color=colors[color_index % len(colors)])  # Cycle through colors
        color_index += 1

axes[0].set_title("Fixed stiffness (Den Hartog)")
axes[0].set_xlabel('Frequency, Hz')
axes[0].set_ylabel('Amplitude, m/s^2/N')
axes[0].legend()
axes[0].grid()

plt.sca(axes[1])  # Select the second subplot

plt.plot(np.abs(freq_range), np.abs(untuned_FRF_calc), label='System without TMD', color='orange')

for m2, c2, k2, mu, z2 in TMD_parameters_by_k_Lin:
    if m2 is not None:  # Ensure m2 was calculated successfully
        tuned_FRF_range = frf.tuned_FRF(freq_range, m1, c1, k1, m2, c2, k2)
        plt.plot(np.abs(freq_range), tuned_FRF_range, 
                 label=f"mu = {mu:.2f}, k2 = {k2:.0f}, m2 = {m2:.6f}, z2 = {z2:.2f}",  # Display mu, k2, m2, z2 in legend
                 color=colors[color_index % len(colors)])  # Cycle through colors
        color_index += 1

axes[1].set_title("Fixed stiffness (Lin)")
axes[1].set_xlabel('Frequency, Hz')
axes[1].set_ylabel('Amplitude, m/s^2/N')
axes[1].legend()
axes[1].grid()

plt.show()
