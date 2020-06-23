"""
Crie um programa que leia o nome completo de uma pessoa e mostre: 
•	O nome com todas as letras maiúsculas e minúsculas.
•	Quantas letras ao todo(sem considerar espaços)
•	Quantas letras tem o primeiro nome.
"""

# inserção dos dados pelo usuário
nome = str(input('Digite o seu nome completo: ')).strip()

# tratamento de strings 
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_junto = ''.join(nome.split())
primeiro_nome = nome.split()[0].capitalize()

print(f'O nome digitado tudo em letras maiúsculas fica: {nome_maiusculo}.')
print(f'O nome digitado tudo em letras minusculas fica: {nome_minusculo}.')
print(f'O nome possui {len(nome_junto)} letras, sem contar os espaços.')
print(f'O primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')
