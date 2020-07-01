"""
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

numero = int(input('Digite um número para mostrar o seu fatorial: '))

print('5! = ', end='')

resultado = 1
while numero >= 1:
    print(f'{numero}', end=' ')
    print('x' if numero > 1 else '=', end=' ')
    resultado *= numero
    numero -= 1
print(resultado)


# usando biblioteca
import math

num = int(input('Digite um número: '))
resultado = math.factorial(num)
print(f'O fatorial do número {num} é {resultado}.')
