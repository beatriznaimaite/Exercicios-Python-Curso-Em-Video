# Faça um programa que leia um ângulo qualquer a mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# importando a biblioteca
import math

# usuário insere os dados
angulo = float(input('Digite o ângulo: '))

# cálculo do seno, cosseno e tangente
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}º tem o seno de {seno:.2f};'
      f'\nO ângulo de {angulo}º tem o cosseno de {cosseno:.2f};'
      f'\nO ângulo de {angulo}º tem a tangente de {tangente:.2f}.')
