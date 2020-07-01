"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True: #while num >= 0:
    num = int(input('Digite o valor para mostrar a tabuada (Para sair, digite um número negativo): '))

    if num < 0:
        print('FINALIZANDO...')
        break

    print('------ TABUADA ------'.center(40))
    for i in range(11):
        print(f'{num:2} x {i:2} = {num * i}'.center(40))
    print('-'*40)
