# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# inserção do dado pelo usuário
metros = float(input('Entre com um valor em metros: '))

# cálculo de conversão (para cm e para mm)
cm = metros * 100
mm = metros * 1000

# exibição da mensagem na tela
print(f'{metros} m equivale a {cm} cm e {mm} mm.')
