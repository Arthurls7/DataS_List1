import numpy as np
from scipy.stats import shapiro

def testeHipotese(array):
    #Aqui faremos o teste de Shapiro-Wilk
    stat, pvalue = shapiro(data)
    if pvalue > 0.05:
        print("Dados fora da normalidade")
    else:
        print("Dados normais")
    
#Abaixo o conjunto de dados e a chamada da função
data = [18,18,19,19,19,20,21,21,22,23]
testeHipotese(data)




