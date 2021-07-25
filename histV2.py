import matplotlib.pyplot as plt
import numpy as np

def histogramPlot(data, bins, width):
    plt.hist(data, density=False, bins=bins, width=1)
    plt.ylabel('Frequency')
    plt.xlabel('Data');
    plt.show()
    
#Classes = 17
#Amplitude = 51-79 = 28
#Obtidos atraves do padrao de histograma

data = [51, 53, 56, 58, 59, 59, 60, 64, 65, 68, 69, 73, 74, 75, 76, 77, 77, 78, 79, 79]
histogramPlot(data, 17, 1.6)
