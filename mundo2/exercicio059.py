"""
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))


while True:
    print('----------------------------------')
    resp = int(input('O que deseja fazer: \n' 
'[ 1 ] Somar\n'
'[ 2 ] Multiplicar\n'
'[ 3 ] Maior\n'
'[ 4 ] Novos Números\n'
'[ 5 ] Sair do Programa\n'
'RESPOSTA: '))

    if resp == 1:
        print(f'A soma foi: {num1 + num2}.')
    elif resp == 2:
        print(f'O produto foi: {num1 * num2}.')
    elif resp == 3:
        if num1 > num2:
            print(f'O {num1} é maior que o {num2}.')
        else:
            print(f'O {num2} é maior que o {num1}.')
    elif resp == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif resp == 5:
        print('FINALIZANDO...')
        break
    else:
        print('Digite um número de 1 a 5!')
