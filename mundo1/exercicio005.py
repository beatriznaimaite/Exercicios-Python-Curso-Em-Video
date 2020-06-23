# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# entrada dos dados
numero = int(input('Digite na tela um número inteiro: '))

# calculo para saber o sucessor e o antecessor.
sucessor = numero + 1
antecessor = numero - 1

# exibição na tela o resultado final.
print(f'O número {numero} tem como antecessor {antecessor} e como sucessor {sucessor}.')
