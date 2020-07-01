"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if 0 < idade <= 9:
    print(f'A idade é: {idade}. \nCategoria: MIRIM.')
elif 9 < idade <= 14:
    print(f'A idade é: {idade}. \nCategoria: INFANTIL.')
elif 14 < idade <= 19:
    print(f'A idade é: {idade}. \nCategoria: JÚNIOR.')
elif 19 < idade <= 25:
    print(f'A idade é: {idade}. \nCategoria: SÊNIOR.')
elif idade > 25:
    print(f'A idade é: {idade}. \nCategoria: MASTER.')
else:
    print(f'O ano informado está negativo. Por favor, digite novamente.')
