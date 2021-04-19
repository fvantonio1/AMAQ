#Antonio Fernandes Valadares  
#11711ECP015


def regraDeHebb(s1,s2,t):
    w = [0, 0]
    b = 0
    limiar = 0
    yteste = []

    for i in range(0,4):
        x1 = s1[i]
        x2 = s2[i]
        y = t[i]



        print("Entrada :",x1,x2)

        w[0] = w[0] + (x1 * y)
        w[1] = w[1] + (x2 * y)
        b = b + y
        print("Novos pesos: w1 =",w[0],"w2 =",w[1],"b =",b)

    print("\nPeso w1 =",w[0],"Peso w2 =",w[1],"bias =",b)
    print("\nTeste da rede neural encontrada: ")
    print("saida esperada: ", t)

    for i in range(0,4):
        yliquido = w[0] * s1[i] + w[1] * s2[i] + b

        if yliquido >= limiar:
            y = 1
        else:
            y = -1

        yteste.append(y)
        print(s1[i],s2[i],y)

    if(yteste == t):
        print("correto!\n")
    else:
        print("incorreto!\n")

if __name__ == "__main__":
    s1 = [1,-1,1,-1]
    s2 = [1,1,-1,-1]

    for i in range(0,16):
        t = f'{i:04b}'
        t.split()
        saida = []
        for i in range(0,4):
            saida.append(int(t[i]))
            if saida[i] == 0:
                saida[i] = -1

        regraDeHebb(s1,s2,saida)




