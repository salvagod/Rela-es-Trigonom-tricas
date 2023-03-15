#Grupo: Vitor Salvadego, Thaíssa Vitória, Kauany Almeida

"""
Usando o Python e as funções trigonométricas disponíveis nesta linguagem de programação e suas bibliotecas
crie uma função que receba um número inteiro n tal que 1 ≤ n ≤ 5 e plote as funções seno, cosseno e tangente
para todos os ângulos possíveis considerando que n representa o número períodos completos.
"""

import math
import matplotlib.pyplot as plot

def plotar_trigonometria(n):
    ### definindo o intervalo da lista em termos de n ###
    intervalo_lista = [lista / 10 for lista in range(int(n * 20 * math.pi) + 1)]
    ### o 20 é para aumentar a resolucao do intervalo da lista e ficar um pouco melhor
    ### e "lista/10" é pra definir os espaçamentos dos valores da lista, tera um valor a cada 0,1 radianos

    ### vetores para as funções trigonométricas ###
    seno_y = [math.sin(lista) for lista in intervalo_lista]
    cosseno_y = [math.cos(lista) for lista in intervalo_lista]
    tangente_y = [math.tan(lista) for lista in intervalo_lista]

    ### nomes nos gráficos ###
    plot.title(f'Funções Trigonométricas para {n} períodos completos')
    plot.xlabel('Ângulo (rad)')
    plot.ylabel('Valor')

    # Plota as funções trigonométricas
    plot.plot(intervalo_lista, seno_y, label='seno')
    plot.plot(intervalo_lista, cosseno_y, label='cosseno')
    plot.plot(intervalo_lista, tangente_y, label='tangente')

    # Adiciona a legenda
    plot.legend()

    # Exibe o gráfico
    plot.show()

n = int(input("Digite um número entre 1 e 5: "))

if n >= 1 and n <= 5:
    plotar_trigonometria(n)
else:
    exit