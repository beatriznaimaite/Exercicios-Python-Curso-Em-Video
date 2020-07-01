"""
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

cont = total = cont1000 = mais_barato = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$ '))
    
    cont += 1
    total += preco
    if preco > 1000:
        cont1000 += 1

    if cont == 1 or preco < mais_barato:
        mais_barato = preco    # se não identificar o mais barato de preço e o produto que foi, o programa vai pegar o ultimo cadastrado
        prod_barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
            
print(f'- O total gasto na compra foi R$ {total:.2f};',
      f'\n- {cont1000} produto(s) custa(m) mais de R$ 1000.00;'
      f'\n- O produto mais barato é {prod_barato} e custa R$ {mais_barato:.2f}.')
