"""
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint
from time import sleep

pc = randint(0, 10)

print('------ JOGO DA ADIVINHAÇÃO ------')
sleep(1)
print('Vou pensar em um número de zero a 10 para você adivinhar...')
sleep(0.5)
print('Só um momento...')
sleep(1)

acertou = False
palpites = 0
while not acertou:
    resp = int(input('Qual número você acha que eu pensei? '))
    palpites += 1
    if resp == pc:
        print(f'ACERTOU! Eu pensei no número {pc} e você digitou o número {resp}, você acertou com {palpites} palpites!')
        acertou = True
    else:
        if resp < pc:
            resp = int(input('Eu pensei em um número MAIOR, chute outro: ')) 
        elif resp > pc:
            resp = int(input('Eu pensei em um número MENOR, chute outro: ')) 
