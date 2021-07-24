import matplotlib.pyplot as plt
import numpy as np

#Classes = 7
#Amplitude = 1.89-1.71 = 0.18
#Intervalo = 10/7

x = [71,71,71,74,80,81,82,82,84,89]
plt.hist(x, density=False, bins=7, width=1.42)
plt.ylabel('Frequency')
plt.xlabel('Weight');
plt.show()
