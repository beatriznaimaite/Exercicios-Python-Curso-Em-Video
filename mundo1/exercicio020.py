"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# importando a biblioteca
import random

# inserção dos dados pelo usuário e posterior adição a lista
alunos = []
for aluno in range(4):
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    alunos.append(nome)

# opção 1 para sortear
ordem = random.sample(alunos, 4)
print(f'A ordem para apresentação será: {ordem}.')

#opção 2 para sortear
random.shuffle(alunos)
print(f'A ordem para apresentação será: {alunos}')
