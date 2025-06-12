import numpy as np

# Own calculations
def untuned_FRF(freq_range, m, c, k):
    # Range of frequencies to analyze
    omega_range = freq_range * 2 * np.pi # Range of frequencies adjusted to be in rad/s

    return (-(omega_range**2)) / (-(omega_range**2)*m + 1j*c*omega_range + k)


def tuned_FRF(freqs, m1, c1, k1, m2, c2, k2):
    FRF = []
     # Compute the FRF over the frequency range
    for freq in freqs:
        omega = 2 * np.pi * freq

        # New calculations 
        amplitude = - omega**2/(- (omega**2)*m1 + 1j*omega*(c1+c2) + k1 + k2 -(c2*1j*omega + k2)**2 / (-(omega**2)*m2 + 1j*omega*c2+k2) )
        
        amplitude = np.abs(amplitude)
        FRF.append(amplitude)

    return FRF