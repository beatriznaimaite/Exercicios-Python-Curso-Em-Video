"""
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

primeiro_termo = int(input('Digite o primeiro termo de uma P.A.: '))
razao = int(input('Digite a razao da P.A.: '))

print(f'Os 10 primeiros termos de uma PA de primeiro termo {primeiro_termo} e razão {razao} são:')

cont = soma = 0
while cont < 10:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    cont += 1
