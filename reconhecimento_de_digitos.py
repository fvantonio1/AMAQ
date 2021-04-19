#Antonio Fernandes Valadares        
## 11711ECP015

## Rede de perceptrons para o reconhecimento de digitos numa matriz de 4x5 pixels

import random
import PySimpleGUI as sg

## DADOS:

x = [   
        [-1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1], # 1
        [-1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1], # 2
        [1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1], # 3
        [1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1,-1], # 4
        [1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1], # 5
        [-1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1], # 6
        [1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1], # 7
        [-1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1], # 8
        [-1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1 ,1], # 9
        [-1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1 , 1, -1] # 0
    ]

y = [
        [1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #resposta para digito 1
        [-1, 1, -1, -1, -1, -1, -1, -1, -1, -1], # 2
        [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1], # 3
        [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1], # 4
        [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1], # 5
        [-1, -1, -1, -1, -1, 1, -1, -1, -1, -1], # 6
        [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1], # 7
        [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1], # 8
        [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1], # 9
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1] # 0
    ]

w = []
bias = []
ciclos = 0

def treina_rede(s, t):
    limiar = 0
    alpha = 1
    global w
    global bias
    flag = 1
    global ciclos
    #w[10][20]
    # inicializa o peso das conexoes com pesos entre -0.5 e 0.5
    for i in range (0, 10):
        aux = []
        for j in range (0, 20):
            aux.append(random.random() - 0.5)
        w.append(aux)
        bias.append(random.random() -0.5)

    while flag == 1:
        flag = 0
        ciclos = ciclos + 1

        for i in range (0 , 10):
            x = s[i]

            y = []
            for j in range (0, 10):
                somatorio = 0
                for k in range (0, len(x)):
                    somatorio = somatorio + x[k] * w[j][k]
                if somatorio + bias[j] >= limiar:
                    y.append(1)
                else:
                    y.append(-1)

            for j in range (0, 10):
                if t[i][j] != y[j]:
                    flag = 1
                    for k in range(0, len(x)):
                        w[j][k] = w[j][k] + (alpha * x[k] * t[i][j])
                    bias[j] = bias[j] + (alpha * t[i][j])


def reconhece_digito(x):
    global w
    global bias
    limiar = 0
    y = []

    for j in range (0, 10):
        somatorio = 0
        for k in range (0, len(x)):
            somatorio = somatorio + x[k] * w[j][k]
        if somatorio + bias[j] >= limiar:
            y.append(1)
        else:
            y.append(-1)
        
    for i in range (0,len(y)):
        if y[i] == 1:
            if i == 9:
                return 0
            else: 
                return i+1
    

#treina_rede(x,y)
#reconhece_digito()

layout = [  [sg.Text("Rede neural para reconhecer digitos")],
            [sg.Button('Treinar rede')],
            [sg.Text(size=(40,1), key='-OUTPUT1-')],
            [sg.Checkbox('', key='1'), sg.Checkbox('', key='2'), sg.Checkbox('', key='3'), sg.Checkbox('', key='4')],
            [sg.Checkbox('', key='5'), sg.Checkbox('', key='6'), sg.Checkbox('', key='7'), sg.Checkbox('', key='8')],
            [sg.Checkbox('', key='9'), sg.Checkbox('', key='10'), sg.Checkbox('', key='11'), sg.Checkbox('', key='12')],
            [sg.Checkbox('', key='13'), sg.Checkbox('', key='14'), sg.Checkbox('', key='15'), sg.Checkbox('', key='16')],
            [sg.Checkbox('', key='17'), sg.Checkbox('', key='18'), sg.Checkbox('', key='19'), sg.Checkbox('', key='20')],
            [sg.Button('Reconhecer número'), sg.Button('Quit')],
            [sg.Text(size=(40,1), key='-OUTPUT2-')]
        ]

window =  sg.Window("Rede neural", layout)

rede_treinada = 0

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Treinar rede':
        treina_rede(x,y)
        rede_treinada = 1
        window['-OUTPUT1-'].update('Rede Treinada!!!')
    if event == 'Reconhecer número':
        if rede_treinada == 0:
            window['-OUTPUT2-'].update('Voce deve treinar a rede antes!!!')
        else:
            x = []
            for i in range(0, 20):
                valor = str(i+1)
                if values[valor]:
                    x.append(1)
                else:
                    x.append(-1)
                y = reconhece_digito(x)
            window['-OUTPUT2-'].update(y)
            
        #reconhe_digito()

window.close()

    