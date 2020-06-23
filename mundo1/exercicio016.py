"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
• Ex: Digite um número: 6.127
• O número 6.127 tem a parte Inteira 6.
"""
# importar função da biblioteca
from math import trunc

# entrada de dados pelo usuário
num_digitado = float(input('Digite um número qualquer: '))

# mostrando a parte inteira usando trunc
numero_int = trunc(num_digitado)

print(f'A parte inteira do número {num_digitado} é {numero_int}.')
