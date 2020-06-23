# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# inserção dos dados pelo usuário
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))

# teste logico
if numero3 < numero1 > numero2:
    print(f'O número {numero1} é o maior número digitado.')
elif numero1 < numero2 > numero3:
    print(f'O número {numero2} é o maior número digitado.')
else:
    print(f'O número {numero3} é o maior número digitado.')
