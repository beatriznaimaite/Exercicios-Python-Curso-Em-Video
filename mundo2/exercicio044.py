"""
Elabore um programa que calcule o valor a ser pago de um produto, considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco_original = float(input('Entre com o preço do produto: R$ '))
pagamento = int(input('Entre com a forma de pagamento:'
                      '\n[1] À vista no dinheiro/cheque;'
                      '\n[2] À vista no cartão;'
                      '\n[3] Em até 2x no cartão;'
                      '\n[4] 3x ou mais no cartão.'
                      '\n RESPOSTA: '))

if pagamento == 1:
    preco_novo = preco_original - (preco_original * 0.1)
elif pagamento == 2:
    preco_novo = preco_original - (preco_original * 0.05)
elif pagamento == 3:
    parcelamento = int(input('Em quantas vezes vai parcelar? '))
    preco_novo = preco_original
    parcela = preco_novo / parcelamento
    print(f'Você dividiu em {parcelamento} vezes e cada parcela sairá no valor de R$ {parcela:.2f}.')
elif pagamento == 4:
    parcelamento = int(input('Em quantas vezes vai parcelar? '))
    preco_novo = preco_original + ( preco_original * 0.2) 
    parcela = preco_novo / parcelamento
    print(f'Você dividiu em {parcelamento} vezes e cada parcela sairá no valor de R$ {parcela:.2f}.')
else:
    preco_novo = 0
    print('VALOR INCORRETO! DIGITE NOVAMENTE... ')

print(f'O preço final do produto ficou em R$ {preco_novo:.2f}.')
