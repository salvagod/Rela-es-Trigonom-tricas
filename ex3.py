#Grupo: Vitor Salvadego, Thaíssa Vitória, Kauany Almeida

"""
Usando o Python e as funções trigonométricas disponíveis nesta linguagem de programação e suas bibliotecas
crie uma função que receba um ângulo, em graus, e plote um circulo trigonométrico de raio 1, centrado na 
origem destacando este ângulo, seu seno, seu cosseno e sua tangente.
"""

import numpy as np
import matplotlib.pyplot as plt

def RealizarTrigonometria(anguloGrau):
    anguloRadiano = np.deg2rad(anguloGrau)

    seno = np.sin(anguloRadiano)
    cosseno = np.cos(anguloRadiano)
    tangente = np.tan(anguloRadiano)

    circulo = plt.Circle((0, 0), 1)

    fig, ax = plt.subplots()

    ax.add_artist(circulo)

    ax.plot([0, cosseno], [0, seno], 'r')

    ax.text(0.8, 1.3, f'sen({anguloGrau}) = {seno:.2f}')
    ax.text(0.8, 1.18, f'cos({anguloGrau}) = {cosseno:.2f}')
    ax.text(0.8, 1.05, f'tan({anguloGrau}) = {tangente:.2f}')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    plt.show()

angulo = int(input("Digite um ângulo: "))
RealizarTrigonometria(angulo)