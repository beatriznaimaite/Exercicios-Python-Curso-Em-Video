"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
•	Ex: Ana Maria de Souza
•	primeiro = Ana
•	último = Souza
"""

# inserção dos dados pelo usuário
nome = str(input('Digite o seu nome inteiro: ')).strip().upper()

# tratamento de strings
nome_separado = nome.split()
primeiro_nome = nome_separado[0].title()
ultimo_nome = nome_separado[-1].title()

print(f'O primeiro nome da pessoa é: {primeiro_nome}.'
      f'\nO último nome da pessoa é: {ultimo_nome}.')
