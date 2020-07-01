"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

cont_maior = cont_menor = 0
for nasc in range(7):
    ano_nasc = int(input('Digite o ano de nascimento da pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'Há {cont_maior} pessoa(s) maior(es) de idade e {cont_menor} pessoa(s) menor(es) de idade.')
