"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

vitorias = 0

while True:
    resp = ' '
    pc = randint(0, 10)
    usuario = int(input('Digite um número: '))
    soma = usuario + pc

    while resp not in 'PI':
        resp = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Eu pensei no número {pc} e você digitou o número {usuario}, total = {soma}.')

    if soma % 2 == 0 and resp == 'P' or soma % 2 == 1 and resp == 'I':
        vitorias += 1
        print('Você ganhou!')
        
    else:
        print(f'Você perdeu')
        break

print(f'Você venceu {vitorias} vez(es)!')
