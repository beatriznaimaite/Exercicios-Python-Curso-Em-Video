# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# importando biblioteca para cálculo da raiz quadrada
from math import sqrt

# informação váriável sendo inserida pelo usuário
numero = int(input('Digite um número inteiro: '))

# realização dos cálculos 
dobro_num = numero * 2
triplo_num = numero * 3
raiz_num = sqrt(numero)

# exibição do resultado na tela
print(f'O número {numero} tem como resultado:', 
    f'\nDobro: {dobro_num}.',
    f'\nTriplo: {triplo_num}.',
    f'\nRaiz Quadrada: {raiz_num}.')
