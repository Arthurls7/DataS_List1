import matplotlib.pyplot as plt
import numpy as np

#Classes = 6
#Amplitude = 23-18 = 5
#Intervalo = 1.2
#Obtidos atraves do padrao de histograma

x = [18,18,19,19,19,20,21,21,22,23]
plt.hist(x, density=False, bins=6, width=1.2)
plt.ylabel('Frequency')
plt.xlabel('Age');
plt.show()
