import matplotlib.pyplot as plt
import numpy as np

def histogramPlot(data, bins, width):
    plt.hist(data, density=False, bins=bins, width=1)
    plt.ylabel('Frequency')
    plt.xlabel('Data');
    plt.show()
    
#Classes = 11
#Amplitude = 30-19 = 11 
#Obtidos atraves do padrao de histograma

data = [19, 19, 20, 20, 21, 22, 22, 23, 24, 25, 26, 26, 27, 29, 29, 29, 29, 30, 30, 30]
histogramPlot(data, 11, 1)
