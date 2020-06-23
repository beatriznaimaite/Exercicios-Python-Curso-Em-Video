"""
Desenvolva um programa que pergunte a distância de uma viagem em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas. 
"""

# inserção dos dados pelo usuário
km = input('Digite a distância da viagem (km): ')

# conversão de tipo e tratamento de string
km = float(km.replace(',','.'))

# teste lógico
if km <= 200:
    preco = km * 0.5
    print(f'O preço da passagem será de R$ {preco:.2f}.')
else:
    preco = km * 0.45
    print(f'O preço da passagem será de R$ {preco:.2f}.')
