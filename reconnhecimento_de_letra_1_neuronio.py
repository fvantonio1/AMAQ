## Antonio Fernandes Valadares
## 11711ECP015

#rede de neural de um neuoronios para o treinamento e reconhecimento de duas letras X e T


# Representação das letras X e T numa matriz de pixels 5x5
X = [1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1] 
T = [1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1]
#tabela verdade
x = [X,
    T]
t = [1,
    -1]

def treinaperceptrons(s,t):
    w = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    bias = 0
    alpha = 1
    limiar = 0
    y_in = 0
    ciclos = 0
    flag = 1

    print("Treinando...")


    while flag == 1:
        flag = 0
        ciclos = ciclos + 1
        print("Ciclo",ciclos,":")


        for i in range(0,len(t)):
            x = s[i]


            for j in range(0,len(x)):
                y_in = y_in + x[j]*w[j]

            y_in = y_in + bias

            if y_in >= limiar:
                y = 1
            else:
                y = -1

            if (y != t[i]):
                flag = 1
                for j in range (0,len(x)):
                    w[j] = w[j] + (alpha * t[i] * x[j])
                bias = bias + (alpha * t[i])

        print("Pesos novos:", w)
        print("Bias novo:",bias)

    print("\n---->Testando a rede neural encontrada: ")
    for i in range (0,len(t)):
        y_liq = 0
        x = s[i]
        for j in range(0,len(x)):
            y_liq = y_liq + x[j]*w[j]

        if y_liq >= limiar:
            y = 1
        else:
            y = -1
        print("Entrada:",x)
        print("Saida esperada:",t[i],", saida da rede neural treinada:",y, "y_liquido",y_liq)

    print("\n---->Teste para outras entradas: ")
    print("Teste para X com ruido na posicao 15: ")
    x = [1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,1]
    y_liq = 0
    for i in range(0, len(x)):
        y_liq = y_liq + x[i]*w[i]

    if y_liq >= limiar:
        y = 1
    else:
        y = -1

    print("Saida: ",y_liq,y)
    


treinaperceptrons(x,t)
        

