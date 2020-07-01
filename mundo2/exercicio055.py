# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maior = menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da pessoa: '))

    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso cadastrado foi {maior:.2f} kg e o menor peso cadastrado foi {menor:.2f} kg.')
