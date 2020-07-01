"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

import math

numero = int(input('Digite um número inteiro: '))


resp = int(input('Você quer converter o número para qual base de conversão?'
                 '\n[1] - BINÁRIO;'
                 '\n[2] - OCTAL;'
                 '\n[3] - HEXADECIMAL.'
                 '\nResposta: '))

if resp == 1:
    binario = bin(numero)
    print(f'O número {numero} convertido para a base binária é: {binario}.')
elif resp == 2:
    octal = oct(numero)
    print(f'O número {numero} convertido para a base octal é: {octal}.')
elif resp == 3:
    hexadecimal = hex(numero)
    print(f'O número {numero} convertido para a base hexadecimal é: {hexadecimal}.')
else:
    print('Valor digitado não é 1, 2 ou 3!')
