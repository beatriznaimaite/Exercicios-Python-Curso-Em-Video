"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""

tot18 = totH = totM20 = 0

while True:
    sexo = resp = ' '
    
    idade = int(input('Digite a idade da pessoa: '))

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 +=1

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('Foram cadastrados:' 
      f'\n - {tot18} pessoa(s) com mais de 18 anos.'
      f'\n - {totH} homem(ns).'
      f'\n - {totM20} mulher(es) com menos de 20 anos.')
