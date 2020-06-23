"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
•	Ex: Digite um número: 1834
•	unidade: 4
•	dezena: 3
•	centena: 8
•	milhar: 1
"""

numero = int(input('Digite um número [0-9999]: '))

# unidade recebe o resto da divisão inteira do numero inserido por 10
unidade = numero % 10
# dezena recebe o resultado da divisão inteira entre o número inserido por 10, esse resultado vai ser dividido por % 10 e ficará com o resto da divisão
dezena = numero // 10 % 10
# dezena recebe o resultado da divisão inteira entre o número e 100, esse resultado vai ser dividido por 10 novamente e pegará o resto dessa divisão
centena = numero // 100 % 10
# recebe o resultado da divisão inteira por 1000
milhar = numero // 1000

print('unidade:', unidade)
print('dezena:', dezena)
print('centena:', centena)
print('milhar:', milhar)
