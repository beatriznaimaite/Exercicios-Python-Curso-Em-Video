# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


frase = str(input('Digite a frase sem acentos: ')).strip().upper().split()

frase_junta = ''.join(frase)
frase_invertida = frase_junta[::-1]

if frase_junta == frase_invertida:
    print('A frase digitada é um PALINDROMO!')
else:
    print('A frase digitada NÃO é um PALINDROMO!')
