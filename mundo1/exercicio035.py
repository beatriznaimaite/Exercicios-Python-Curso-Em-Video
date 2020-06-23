# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# inserção dos dados pelo usuário 
r1 = float(input('Digite a 1ª reta: '))
r2 = float(input('Digite a 2ª reta: '))
r3 = float(input('Digite a 3ª reta: '))

# teste logico
if (r1 + r2) < r3 or (r2 + r3) < r1 or (r3 + r1) < r2:
    print(f'As retas informadas não formam um triângulo!')
else:
    print(f'As retas informadas formam um triângulo!')
