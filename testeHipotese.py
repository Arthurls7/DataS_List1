import numpy as np
from scipy.stats import shapiro

def testeHipotese(array):
    #Aqui faremos o teste de Shapiro-Wilk
    stat, pvalue = shapiro(array)
    if pvalue > 0.05:
        print("Dados fora da normalidade")
    else:
        print("Dados normais")
    
#Abaixo o conjunto de dados e a chamada da função
data1 = [19, 19, 20, 20, 21, 22, 22, 23, 24, 25, 26, 26, 27, 29, 29, 29, 29, 30, 30, 30]
data2 = [51, 53, 56, 58, 59, 59, 60, 64, 65, 68, 69, 73, 74, 75, 76, 77, 77, 78, 79, 79]
testeHipotese(data1)
testeHipotese(data2)
