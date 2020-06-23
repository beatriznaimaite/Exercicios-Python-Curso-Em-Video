"""Faça um programa que leia uma frase pelo teclado e mostre: 
•	Quantas vezes aparece a letra ‘A’
•	Em que posição ela aparece a primeira vez
•	Em que posição ela aparece a última vez
"""

frase = str(input('Digite uma frase: ')).strip().lower()

total_a = frase.count('a')
primeiro_a = frase.find('a')+1
ultimo_a = frase.rfind('a')+1

print(f"A letra 'a' apareceu {total_a} vezes.")
print(f"A letra 'a' aparece pela primeira vez na posição {primeiro_a}.")
print(f"A letra 'a' aparece pela ultima vez na posição {ultimo_a}.")
