# Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.

# inserção dos dados pelo usuário
nome = str(input('Digite o nome da pessoa: ')).strip().upper()

# teste lógico
if 'SILVA' in nome:
    print('A pessoa tem SILVA no nome.')
else:
    print('A pessoa não tem SILVA no nome.')
