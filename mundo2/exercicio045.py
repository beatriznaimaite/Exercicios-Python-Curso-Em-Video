# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)

print('------ JOKEMPÔ ------'.center(30))
sleep(1)
print('Vamos jogar...')
sleep(1)
jogador = str(input('Escolha: PEDRA, PAPEL OU TESOURA: ')).strip().lower()

if (pc == 'pedra' and jogador == 'tesoura') or (pc == 'tesoura' and jogador == 'papel') or (pc == 'papel' and jogador == 'pedra'):
    print(f'O computador venceu! {pc} ganha de {jogador}!')
elif (jogador == 'pedra' and pc == 'tesoura') or (jogador == 'tesoura' and pc == 'papel') or (jogador == 'papel' and pc == 'pedra'):
    print(f'Você venceu! {jogador} ganha de {pc}!')
elif jogador == pc:
    print(f'EMPATE! Você escolheu {jogador} e o computador escolheu {pc}.')
else:
    print('Valor não encontrado!')
