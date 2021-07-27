from sklearn.datasets import load_iris #Carregar o Iris
from sklearn.model_selection import train_test_split #Separar o conjunto de dados
from sklearn.model_selection import cross_val_score #Calcular com F-measure
from sklearn import metrics #Mostrar os testes
from sklearn.naive_bayes import GaussianNB #Naive Bayes
from sklearn import neighbors #K-NN

n_neighbors = 3 #Valores de vizinhos definidos para o calculo do KNN

X, y = load_iris(return_X_y = True) #X corresponde aos valores e Y aos tipos de flores

gnb = GaussianNB()#Instanciando o Naive Bayes Gaussiano
knn = neighbors.KNeighborsClassifier(n_neighbors) #Instanciando Naive-Bayes

#Aqui dividimos o conjunto em 5, para o realizar a K-Fold cross validation
#Definimos o parametro de score como F1-Score (f1_weighted) como pedido na questão
scoresGNB = cross_val_score(gnb, X, y, cv=5, scoring = 'f1_weighted')
scoresKNN = cross_val_score(knn, X, y, cv=5, scoring = 'f1_weighted')

#Resultados dos testes
j = 1
print("Naive Bayes Results:")
for i in scoresGNB:
    print(f'Test {j} --> {i:3f}')
    j = j+1


j = 1
print("\nK-NN Results:")
for i in scoresKNN:
    print(f'Test {j} --> {i:3f}')
    j = j+1

#Comparando os resultados
print("\nComparison Tests:")
print("-------------------------")

knnLoop = scoresKNN
gnbLoop = scoresGNB

for i in range(0, 5):
    if (scoresKNN[i] - scoresGNB[i]) > 0:
        print("KNN is better in this test")
        print(f'Advantage percentage: {scoresKNN[i] - scoresGNB[i]:3f}')
    elif (scoresKNN[i] - scoresGNB[i]) < 0:
        print("GNB is better in this test")
        print(f'Advantage percentage: {scoresGNB[i]-scoresKNN[i]:3f}')
    else:
        print("In this test, the two classifiers have the same result")

    print("-------------------------")

#Codigos para fazer o uso dos classificadores sem o KFOLD e o F1-score

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#Splita o conjunto de teste em 30% e o de treino em 70%
    
#y_pred = gnb.fit(X_train, y_train).predict(X_test)
#Faz o treino do Naive Bayes
    
#knn.fit(X, y)
#Faz o treino do K-NN




