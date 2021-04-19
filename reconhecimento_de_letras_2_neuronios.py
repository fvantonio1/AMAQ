## Antonio Fernandes Valadares
## 11711ECP015

#rede de neural de dois neuoronios para o treinamento e reconhecimento de duas letras X e T



X = [1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1]
T = [1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1]
T1 = [1,-1]
T2 = [-1,1]
# tabela verdade 
x = [X,
    T]
y = [1, -1
    -1, 1]


def treinaperceptrons(s1,t1,t2):
    #s1 = [X,T]
    #t1 = [1,-1]
    #t2 = [-1, 1]



    w1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    w2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    bias1 = 0
    bias2 = 0
    alpha = 1
    limiar = 0
    ciclos = 0
    flag = 1

    while flag == 1:
        flag = 0
        ciclos = ciclos + 1
        print("Ciclo :",ciclos)


        for i in range (0, len(t1)):
            x = s1[i]
            y_in1 = 0
            y_in2 = 0

            for j in range (0,len(x)):
                y_in1 = y_in1 + x[j]*w1[j]
                y_in2 = y_in2 + x[j]*w2[j]

            y_in1 = y_in1 + bias1
            y_in2 = y_in2 + bias2 
       
            if y_in1 >= limiar:
                y1 = 1
            else:
                y1 = -1
            if y_in2 >= limiar:
                y2 = 1
            else:
                y2 = -1


            if (y1 != t1[i]):
                flag = 1
                for j in range (0,len(x)):
                    w1[j] = w1[j] + (alpha*x[j]*t1[i])
                bias1 = bias1 + (alpha*t1[i])

            if (y2 != t2[i]):
                flag = 1
                for j in range (0,len(x)):
                    w2[j] = w2[j] + (alpha*x[j]*t2[i])
                bias2 = bias2 + (alpha*t2[i])

        print("Pesos novos do neuronio 1:",w1)
        print("Bias novo do neuronio 1:",bias1)
        print("Pesos novos do neuronio 2:",w2)
        print("Bias novo do neuronio 2:",bias2)


    print("\n ---------->Testando a rede neural encontrada :")
    for i in range (0,len(t2)):
        y_liq1 = 0
        y_liq2 = 0

        x = s1[i]

        for j in range(0,len(x)):
            y_liq1 = y_liq1 + x[j]*w1[j]
            y_liq2 = y_liq2 + x[j]*w2[j]

        if y_liq1 >= limiar:
            y1 = 1
        else:
            y1 = -1

        if y_liq2 >= limiar:
            y2 = 1
        else:
            y2 = -1

        print("Entrada:",x)
        print("Saida esperada:",t1[i],"|",t2[i])
        print("Saida da rede neural treinada:",y1,"|",y2)


treinaperceptrons(x,T1,T2)
