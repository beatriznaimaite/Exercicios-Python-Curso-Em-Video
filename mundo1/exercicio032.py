# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# inserção dos dados pelo usuário
ano = int(input('Digite o ano para descobrir se ele é bissexto: '))

# teste lógico
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO!')
else:
    print(f'O ano NÃO É BISSEXTO!')
