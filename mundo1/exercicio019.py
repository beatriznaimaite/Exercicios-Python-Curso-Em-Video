"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

# importando a biblioteca
import random

# usuário insere os dados e inserção dos mesmos em uma lista 
nomes = []
for alunos in range(0, 4):
    aluno = str(input('Digite o nome do aluno: ')).strip().capitalize()
    nomes.append(aluno)

# sorteio do aluno 
resultado = random.choice(nomes)

print(f'O aluno sorteado foi: {resultado}.')
