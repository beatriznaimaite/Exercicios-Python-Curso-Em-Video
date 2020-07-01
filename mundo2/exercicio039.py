"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

ano_nasc = int(input('Entre com o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade >= 18:
    anos = idade - 18
    ano_alist = ano_atual - anos
    print('Você já passou do tempo de alistamento.'
          f'\nPassaram-se {anos} anos, você devia ter se alistado em {ano_alist}.')

elif idade == 18:
    print(f'Você está no período de alistamento!')
else:
    anos = 18 - idade
    ano_alist = ano_atual + anos
    print('Você ainda não está no período de alistamento militar!'
          f'\nFaltam {anos} anos para seu alistamento, o que aconterá no ano de {ano_alist}.')
