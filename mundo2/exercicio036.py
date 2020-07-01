""" 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

salario = float(input('Entre com o salário: R$ '))
valor_casa = float(input('Digite o valor da casa: R$ '))
ano_pagamento = int(input('Em quantos anos você irá pagar? '))


pagamento_mensal = (valor_casa / ano_pagamento) / 12
salario_percent = salario * 0.3


if pagamento_mensal > salario_percent:
    print(f'EMPRÉSTIMO NEGADO! O valor informado mensalmente ultrapassou 30% do salário!'
          f'\nO pagamento será de R$ {pagamento_mensal:.2f} por mês!')
else:
    print(f'EMPRESTIMO APROVADO! O valor não ultrapassará 30% do salário!'
          f'\nO pagamento seria de R$ {pagamento_mensal:.2f} por mês!')
