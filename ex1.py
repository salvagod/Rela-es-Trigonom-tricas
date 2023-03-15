#Grupo: Vitor Salvadego, Thaíssa Vitória, Kauany Almeida

"""
Um fotógrafo está posicionado em frente a uma plataforma de lançamento de foguetes de forma que o eixo da lente da sua câmera está a
50 m de distância e perfeitamente alinhada com a base do foguete. Em que ângulo ele deve colocar a câmera para tirar uma foto deste 
foguete quando ele estiver há 200 m de altura. 
"""

import math
import matplotlib.pyplot as plt

loop = True
distancia_fixa = 50

alturas = [200]

def CalcularAngulo(altura, distancia_fixa):
    anguloRadiano = math.atan(altura/distancia_fixa)
    anguloGrau = math.degrees(anguloRadiano)

    alturas.append(altura)
    
    return anguloGrau

#C) Plotar, usando a biblioteca Matplotlib um diagrama do triângulo resultante em cada altitude

def FazerDiagrama(altura, distancia_fixa):
    angulo = CalcularAngulo(altura, distancia_fixa)

    x = [0, distancia_fixa, distancia_fixa]
    y = [0, 0, altura]

    plt.plot(x, y)
    plt.title(f"Altura do foguete: {altura} m | Ângulo: {angulo:.2f} graus")
    plt.xlabel("Distância da câmera à base do foguete (m)")
    plt.ylabel("Altura do foguete (m)")
    plt.show()

#A) Encontrar o ângulo da câmera usando os dados iniciais (200m de altura e 50m de distância)

angulo = math.atan(200/distancia_fixa)
anguloGrau = math.degrees(angulo)

print("A altura é 200m")
print("O ângulo necessário é de", anguloGrau, "graus")

#B) Função para ajustar o ângulo para qualquer altitude (Pelo enunciado, somente a altitude muda, não mudando a distância)

while loop == True:

    if loop == False:
        exit
    resposta = input("Deseja ajustar a câmera com novos valores? ")

    if resposta == "Sim":
        altura = float(input("Digite a altura em metros: "))

        resultado = CalcularAngulo(altura, distancia_fixa)

        print("O ângulo da câmera precisa ser de", resultado, "graus")

    else:
        for i in range(len(alturas)):
            altura = alturas[i]
            FazerDiagrama(altura, distancia_fixa)
        
        loop = False