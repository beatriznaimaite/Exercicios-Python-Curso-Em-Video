"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
"""

# entrada de dados
km_percorrido = float(input('Digite a quantidade de quilometros percorridos por um carro: '))
dias_alugado = int(input('O carro foi alugado por quantos dias? '))

# cálculo dos valores
total_km = km_percorrido * 0.15
total_dias = dias_alugado * 60
total_gasto = total_km + total_dias

print(f'Você gastou R$ {total_gasto:.2f} ao todo, sendo o total de R$ {total_km:.2f} pelos quilômetros e R$ {total_dias:.2f} por dias alugados.')