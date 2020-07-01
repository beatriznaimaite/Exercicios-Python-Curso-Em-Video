"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'A média do aluno foi: {media:.2f}.'
           '\nSituação: REPROVADO!')
elif 5 <= media < 7:
    print(f'A média do aluno foi: {media:.2f}.'
           '\nSituação: RECUPERAÇÃO!')
elif 7 <= media <= 10:
    print(f'A média do aluno foi: {media:.2f}.'
           '\nSituação: APROVADO!')
else:
    print('A média digitada foi maior que 10! Por favor, digite novamente!')
