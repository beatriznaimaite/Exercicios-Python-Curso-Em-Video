"""
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

num = int(input('Digite quantos termos você quer ver da sequência de Fibonacci: '))

anterior = 0
proximo = 0
cont = 0
while cont < num:
    print(proximo, end=' ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1
    cont += 1
