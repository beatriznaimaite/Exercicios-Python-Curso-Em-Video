"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 
"""

# inserção dos dados pelo usuário
salario = input('Entre com o salario do funcionário: R$ ')

# conversão de string e tipo de dados
salario = float(salario.replace(',','.'))

# teste lógico
if salario > 1250.00:
    novo_salario = salario + (salario * 0.1)
    aumento = novo_salario - salario
else:
    novo_salario = salario + (salario * 0.15)
    aumento = novo_salario - salario

print(f'Com o reajuste, o salário passou a ser de R$ {novo_salario:.2f}, tendo um aumento de R$ {aumento:.2f}.')
