"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

print(f'Os 10 primeiros termos de uma PA de primeiro termo {primeiro_termo} e razão {razao} são:')
for num in range(10):
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
