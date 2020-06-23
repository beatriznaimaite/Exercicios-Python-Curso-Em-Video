"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# importando as bibliotecas
import random
from time import sleep

# sorteio do número pelo computador
pc = random.randint(0, 5)

# cógigo para aumentar a interatividade do usuário
print('-------- Jogo de Adivinhação --------'.center(60))
print('Vou pensar em um número entre 0 a 5 e você vai tentar adivinhar...')
sleep(1)
print('Só um momento...')
sleep(1)
print('Pronto, já pensei!')

# inseção dos dados pelo usuário
usuario = int(input('Digite o número que eu pensei: '))

# teste lógico
if usuario == pc:
    print(f'ACERTOU!!! Eu pensei no número {pc} e você digitou o número {usuario}!')
else:
    print(f'ERROU!!! Eu pensei no número {pc} e você digitou o número {usuario}!')
