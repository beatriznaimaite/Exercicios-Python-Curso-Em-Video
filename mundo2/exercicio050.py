"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0
lista = []
for num in range(6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        lista.append(numero)
        soma += numero

print(f'Os números digitados foram: {lista} e a soma dos números digitados foi {soma}.')
