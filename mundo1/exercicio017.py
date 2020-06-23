# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule o mostre o comprimento da hipotenusa.

# importando a biblioteca
import math

# informação inserida pelo usuário
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o cateto adjacente: '))

# cálculo da hipotenusa
hipotenusa = math.sqrt((cat_oposto ** 2) + (cat_adjacente ** 2))

print(f'Com o valor {cat_oposto} do cateto oposto e com o valor {cat_adjacente} do cateto adjacente, obtemos uma hipotenusa de resultado {hipotenusa:.2f}.')
