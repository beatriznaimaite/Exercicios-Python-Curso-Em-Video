"""
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
num = int(input('Digite um número para saber a tabuada: '))

print('------ TABUADA ------'.center(40))
for i in range(11):
    print(f'{num:2} x {i:2} = {num * i:2}'.center(40))
