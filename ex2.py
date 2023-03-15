#Grupo: Vitor Salvadego, Thaíssa Vitória, Kauany Almeida

"""
O código de construção civil determina a inclinação mínima dos telhados de acordo com o clima da região. 
Na maior parte das vezes esta inclinação mínima é para evitar excesso de peso sobre a estrutura no caso de
chuva, ou neve. No Brasil, a inclinação de telhados é determinada pela norma NBR 5720 que permite algumas 
variações de acordo com o tipo de telha escolhido para a cobertura. No caso de telhas cerâmicas, a norma 
que deve ser utilizada é a norma NBR 8039. Esta norma determina que a inclinação mínima para cada telhado
deverá ser de 25% . Sabendo que este percentual relaciona a altura com o comprimento do telhado, calcule a 
altura que um telhado com 3 m deverá ter para atender esta norma.
"""

import math
import matplotlib.pyplot as plt

# B) Criar função para definir altura
def CalcularAltura(comprimento):
    altura = comprimento * inclinacao
    return altura

# A) Encontrar a altura pedida pelo enunciado
comprimento = 3
inclinacao = 0.25
altura = comprimento * inclinacao
print("A altura mínima do telhado é de", altura, "metros")

# C) Criar o diagrama mostrando a altura necessária e ângulo para o telhado, entre 2 e 7 metros
comprimentos = range(2, 8)
alturas = [CalcularAltura(i) for i in comprimentos]
angulos = [round(math.degrees(math.atan(j/i)), 2) for j, i in zip(alturas, comprimentos)]

plt.plot(comprimentos, alturas)
plt.xlabel('Comprimento (m)')
plt.ylabel('Altura (m)')
plt.title('Diagrama do Telhado (2 a 7 metros)')
plt.text(4.58, 0.5, f'Ângulos: {angulos}°', ha='center', va='center')
plt.show()