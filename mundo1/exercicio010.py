# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27.

# definição do valor a partir da entrada do usuário.
valor_carteira = float(input('Digite quanto de dinheiro você tem em sua carteira: R$ '))

# cálculo de conversão de real para dólar
total_dolar = valor_carteira / 3.27

# exibição da mensagem na tela
print(f'Com R$ {valor_carteira:.2f} você consegue comprar US$ {total_dolar:.2f}.')
