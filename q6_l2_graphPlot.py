import matplotlib.pyplot as plt
import numpy as np

recebidos = [160, 184, 241, 149, 180, 161, 132, 202, 160, 139, 149, 177]
processados = [160, 184, 237, 148, 181, 150, 123, 156, 126, 104, 124, 140]

x1 =  np.arange(len(recebidos))
x2 = [x + 0.25 for x in x1]

plt.bar(x1, recebidos, width=0.25, label = 'Recebidos', color = 'b')
plt.bar(x2, processados, width=0.25, label = 'Processados', color = 'y')

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago','Set','Out','Nov','Dez']
plt.xticks([x + 0.25 for x in range(len(recebidos))], meses)

plt.title("Gráfico de recebidos e processados")
plt.show()
