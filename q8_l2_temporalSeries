import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

#Git import csv
url = 'https://raw.githubusercontent.com/bapimentel/Ciencia-de-Dados/master/Dados/Drugs.csv'
df = pd.read_csv(url, parse_dates=['date'], index_col='date')

#Additive Decomposition
result_add = seasonal_decompose(df['value'], model='additive', extrapolate_trend='freq')

#Plot
plt.rcParams.update({'figure.figsize': (10,10)})
result_add.plot().suptitle('Additive Decompose', fontsize=22)
plt.show()
