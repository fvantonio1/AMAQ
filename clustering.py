from os import stat
import matplotlib.pyplot as plt
import numpy as np
import math
import random

f = open('observacoescluster.txt', 'r')

pontos = []
for linha in f:
    ponto = linha.split()
    ponto[0] = float(ponto[0])
    ponto[1] = float(ponto[1])
    pontos.append(ponto)
f.close()


def start_centroidsplus(pontos, k):
    centroids = []
    for i in range(0, k):
        x = random.randint(0, len(pontos))
        centroids.append(pontos[x])
    return centroids


#Função para iniciar as centroides
def start_centroids(k, maximo):
    centroids = []
    for i in range(0,k):
        centroids.append([random.random()*10, random.random()*10])
        
    return centroids


#Função que retornas as distancias e a centroide mais proxima de cada ponto
def closest_centroid(pontos, centroids):
    distancias = []
    grupos = []
    for i in range(0, len(pontos)):
        maisproximo = 1000

        for j in range(0, len(centroids)):
            d = ((pontos[i][0] -  centroids[j][0])**2) + ((pontos[i][1] - centroids[j][1])**2)
            distancia = math.sqrt(d)

            if distancia < maisproximo:
                maisproximo = distancia
                centroide_maisproxima = j

        distancias.append(maisproximo)
        grupos.append(centroide_maisproxima)


    return distancias, grupos


#Função para retornar as novas centroids
def update_centroids(pontos, centroids, grupos):
    novas_centroids = []
    for i in range(0, len(centroids)):
        soma = [0,0]
        elementos = 0
        for j in range(0, len(pontos)):
            if grupos[j] == i:
                soma[0] += pontos[j][0]
                soma[1] += pontos[j][1]
                elementos += 1
        if elementos != 0:
            soma[0] = soma[0] / elementos
            soma[1] = soma[1] / elementos
        novas_centroids.append(soma)

    return novas_centroids

def plot_cluster(pontos, centroids, grupos):
    for i in range(0, len(pontos)):
        if(grupos[i] == 0):
            plt.plot(pontos[i][0], pontos[i][1], 'p', color='red')
        if(grupos[i] == 1):
            plt.plot(pontos[i][0], pontos[i][1], 'p', color='blue')
        if(grupos[i] == 2):
            plt.plot(pontos[i][0], pontos[i][1], 'p', color='yellow')
        if(grupos[i] == 3):
            plt.plot(pontos[i][0], pontos[i][1], 'p', color='green')

    for i in range(0, len(centroids)):
        plt.plot(centroids[i][0], centroids[i][1], 'p', color='black')
    plt.show()


def k_means(pontos, n_centroids):
    ciclos = 0
    flag = 0
    leqt = []

    #centroids = start_centroids(n_centroids, 10)
    centroids = start_centroidsplus(pontos,n_centroids)

    while(flag == 0):

        distance, grupos = closest_centroid(pontos, centroids)

        novas_centroids = update_centroids(pontos, centroids, grupos)


        eqt = 0
        for i in range(0, len(distance)):
            eqt += distance[i]**2
        leqt.append(eqt)

        if(novas_centroids == centroids):
            flag = 1

        centroids = novas_centroids

        ciclos += 1

    print(ciclos)
    plot_cluster(pontos, centroids, grupos)
    plt.plot(leqt)
    plt.show()
    print(leqt)



k_means(pontos, 4)



# for i in range(0, len(pontos)):
#     plt.plot(pontos[i][0], pontos[i][1], 'p', color='red')

# centroids = start_centroids(4,10)

# for i in range(0, len(centroids)):
#     plt.plot(centroids[i][0], centroids[i][1], 'p', color='blue')
# plt.show()

# distancias, grupos = closest_centroid(pontos,centroids)
# novas_centroids = update_centroids(pontos,centroids,grupos)

# for i in range(0, len(pontos)):
#     plt.plot(pontos[i][0], pontos[i][1], 'p', color='red')
# for i in range(0, len(novas_centroids)):
#     plt.plot(novas_centroids[i][0], novas_centroids[i][1], 'p', color='blue')
# plt.show()
