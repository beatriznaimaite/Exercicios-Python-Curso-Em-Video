# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. 

# inserção dos dados pelo usuário
numero = int(input('Digite um número inteiro: '))

# teste lógico
if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')
