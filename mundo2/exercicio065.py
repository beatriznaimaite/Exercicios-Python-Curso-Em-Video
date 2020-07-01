"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

resposta = 'S'
cont = soma = maior = menor = media = 0
while resposta == 'S':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        resposta = False
        print('Finalizando...')

media = soma/cont

print(f'A média entre os valores lidos foi de {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor {menor}.')
