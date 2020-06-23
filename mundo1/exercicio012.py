# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# entrada do valor pelo usuário
preco_inicial = float(input('Digite o preço do produto: R$ '))

# cálculo de desconto e economia
preco_desconto = preco_inicial - (preco_inicial * 0.05)  # 0.05 = 5/100
economia = preco_inicial - preco_desconto

# exibição do valor na tela
print(f'Com o desconto de 5%, o produto passará a custar R$ {preco_desconto:.2f}. Você economizou R$ {economia:.2f}!!')
