# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# entrada de dados realizado pelo usuário
salario_atual = float(input('Entre com o salário atual do funcionário: R$ '))

# cálculo do novo salário e total em reais que ele receberá a mais.
salario_aumento = salario_atual + (salario_atual * 0.15)  # 0.15 = 15/100
total_aumento = salario_aumento - salario_atual

# exibição do valor na tela
print(f'O salário do funcionário passará a ser de: R$ {salario_aumento:.2f}, tendo um incremento de R$ {total_aumento:.2f}.')
