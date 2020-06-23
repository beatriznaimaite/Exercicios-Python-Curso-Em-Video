# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# entrada das notas pelo usuário
nota1 = float(input('Entre com a primeira nota do aluno: '))
nota2 = float(input('Entre com a segunda nota do aluno: '))

# cálculo da média
media = (nota1 + nota2) / 2

# exibição da mensagem final
print(f' A média do aluno foi de: {media:.1f}.')
