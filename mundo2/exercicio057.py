"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Digite o sexo da pessoa (use apenas M ou F): ')).strip()

while sexo not in 'MmFf':
    sexo = str(input('Valor incorreto. Digite o sexo da pessoa: '))

print(f'Você digitou corretamente. Sexo validado!')
