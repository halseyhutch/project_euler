import numpy as np


# https://en.wikipedia.org/wiki/Fibonacci_number#Magnitude
# slightly improved
def p25(nd):
    phi = 0.5*(1 + np.sqrt(5))
    # drop the (-phi)^-n, very small for any semi large n
    # nd = log10(phi^n/sqrt(5)) + 1 [find n]
    return round((nd + 0.5*np.log10(5) - 1)/np.log10(phi))


print(p25(1000))