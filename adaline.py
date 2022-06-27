import random
import pandas as pd
import matplotlib.pyplot as plt

#Pega os dados da tabela no excel para o treinamento
X = []
Y = []

df_treinamento = pd.read_excel('Tabela de treinamento Adaline.xls', header = 1)

Y = df_treinamento['d']

for i in range(0,35):
    aux = []
    item = df_treinamento.iloc[i]
    aux.append(item[0])
    aux.append(item[1])
    aux.append(item[2])
    aux.append(item[3])
    X.append(aux)

#Pega os dados da tabela no excel para o teste
X_teste = []

df_teste = pd.read_excel('Tabela4.3_Testes.xls', header = 2)

for i in range(0,15):
    aux = []
    item = df_teste.iloc[i]
    aux.append(item[0])
    aux.append(item[1])
    aux.append(item[2])
    aux.append(item[3])
    X_teste.append(aux)


##################

w = []
bias = 0

#Função de treinamento do adaline
def treinaAdaline(s, t):
    global bias
    
    #inicia w e o bias com pesos aleatórios entre 0 e 1
    for i in range(0,len(s[0])):
        w.append(random.random())
    bias = random.random()
    print("Pesos iniciais: ",w,"bias: ",bias)

    #define a taxa de aprendizagem
    alpha = 0.0025

    #define a precisão
    precisao = 0.000001

    ciclos = 0
    flag = 1
    erqt = []
    
    #laço até que o erro seja menor que a precisao
    while(flag == 1):
        flag = 0
        ciclos = ciclos + 1
        erro = 0

        wanterior = []
        wanterior.append(w[0])
        wanterior.append(w[1])
        wanterior.append(w[2])
        wanterior.append(w[3])

        #apresenta todas entradas
        for i in range(0, len(t)):
            x = s[i]
            y = t[i]
            erroquadratico = 0

            #calcula saída liquida
            y_in = bias
            for j in range(0, len(x)):
                y_in = y_in + x[j]*w[j]

            erroquadratico = erroquadratico + (y_in - y) * (y_in - y)

            #atualiza os pesos de w e do bias e verifica a maior mudança de pesos
            for j in range(0, len(x)):
                w[j] = w[j] + alpha * (t[i] - y_in) * x[j]
            bias = bias + alpha * (t[i] - y_in)

        #Cria um vetor com os erros quadraticos de cada ciclo
        erqt.append(erroquadratico)



        #verifica o maior erro
        for i in range(0,4):
            if abs(wanterior[i]-w[i]) > erro:
                erro = abs(wanterior[i]-w[i])

        #caso o erro seja maior que a precisao desejada o algortimo continua
        if erro > precisao:
            flag = 1

    print("Pesos finais: ",w,"bias: ",bias)
    print("Número de ciclos: ",ciclos)
 
    #Plota o gráfico do erro quadrático
    #plt.plot(erqt)
    #plt.show()

#Função para responder a valores de entrada
def testaAdaline(s):
    limiar = 0

    for i in range(0,len(s)):
        x = s[i]
        y_in = bias
        for j in range(0, len(x)):
            y_in = y_in + x[j]*w[j]

        if y_in > limiar:
            print("Vávula A")
        else:
            print("Válcula B")




treinaAdaline(X,Y)
testaAdaline(X_teste)






