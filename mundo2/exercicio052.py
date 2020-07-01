# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se ele é primo: '))


cont_num = 0
for i in range(1, num+1):
    if num % i == 0:
        cont_num += 1
    
if cont_num == 2:
    print(f'O número {num} É PRIMO! Ele é divisível por {cont_num} números.')
else:
    print(f'O número {num} NÃO É PRIMO! Ele é divisível por {cont_num} números.')
