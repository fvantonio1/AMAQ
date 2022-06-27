import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]]).reshape(11,1)
Y = np.array([[-0.9602, -0.5770, -0.729, 0.3771, 0.6405, 0.66, 0.4609, 0.1336, -0.2013, -0.4344, -0.5]]).reshape(11,1)

class RedeNeural:
    def __init__(self, entrada, saida, neuronios_escondidos, alpha = 0.01, ciclos = 1000):
        self.X = entrada
        self.Y = saida
        self.hidden = neuronios_escondidos
        self.alpha =  alpha
        self.erro = 0.001
        self.ciclos = ciclos
        self.m = self.X.shape[1]

        #Pesos da camada escondida
        self.w1 = np.random.rand(self.X.shape[1], self.hidden) - 0.5
        self.bw1 = np.random.rand(1, self.hidden) - 0.5

        self.delta1 = np.zeros((self.hidden, 1))

        #Pesos da camada de saida
        self.w2 = np.random.rand(self.hidden, self.Y.shape[1]) - 0.5
        self.bw2 = np.random.rand(self.Y.shape[1], 1) - 0.5

        self.delta2 = np.zeros((self.Y.shape[1], 1))


    #Função de ativação
    def sigmoide_bipolar(self, z1):
        return (2/(1+np.exp(-z1))) -1

    #Parcial da Função de ativação        
    def sigmoide_parcial(self, z2):
        return (0.5 * (1 + z2) * (1 - z2))

    #Feedforward
    def feed_forward(self, X):

        #propaga a entrada para os neuronios escondidos
        self.zin = np.dot(X, self.w1) + self.bw1     ##X * w + b
        self.z = self.sigmoide_bipolar(self.zin)    #z = f(zin)

        #cacula a saída
        self.yin = np.dot(self.z, self.w2) + self.bw2
        self.y = self.sigmoide_bipolar(self.yin) 
        print(self.y)       

        return self.y

    def retropropagation(self):
        
        #Calculo do erro da camada de saída(deltinha)
        self.da2 = self.Y - self.y 
        self.delta2 = self.da2 * self.sigmoide_parcial(self.y) ###yin ou y?

        #Calculo do erro da camada escondida(deltinha)
        self.da1 = self.delta2.dot(self.w2.T)
        self.delta1 = self.da1 * self.sigmoide_parcial(self.zin) ##zin ou z?


        #Delta dos pesos da camada de saída
        self.dEdW2 = self.alpha * (self.z.T.dot(self.delta2))
        self.dEdBw2 = np.sum(self.alpha * self.delta2, axis=0)

        #Delta dos pesos da camada escondida
        self.dEdW1 = self.alpha * (self.X.T.dot(self.delta1))
        self.dEdBw1 = np.sum(self.alpha * self.delta1, axis=0)


        #Atualiza os pesos da camada de saída
        self.w2 += self.dEdW2
        self.bw2 += self.dEdBw2

        #Atualiza os pesos da camada de de entrada
        self.w1 += self.dEdW1
        self.bw1 += self.dEdBw1

    def train(self):
        ciclo = 0
        erro_total = 0
        self.erros = []
        while(ciclo < self.ciclos) or (erro_total < self.erro):
            erro_total = 0
            y = self.feed_forward(self.X)
            self.retropropagation()

            erro_total += sum(0.5 * ((self.Y - y)**2))
            self.erros.append(erro_total)

            ciclo += 1

        tam = len(self.erros)
        X_grid = np.array(np.arange(0, tam))
        plt.scatter(X_grid, self.erros)
        plt.show()

        


nn = RedeNeural(X, Y, 6)
# print(nn.w1)
# print(X)

nn.train()
# print(X)
# print(Y)
# print(nn.feed_forward(X))

# print(nn.w1)
# print(nn.bw1)
# print(nn.w2)
# print(nn.bw2)
# k = np.linspace(-10, 10, 100)
# plt.plot(k, nn.sigmoide_parcial(k))
# plt.show()