"""
Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

reta1 = float(input('Digite a 1ª reta: '))
reta2 = float(input('Digite a 2ª reta: '))
reta3 = float(input('Digite a 3ª reta: '))


if reta1 > reta2 + reta3 or reta2 > reta1 + reta3 or reta3 > reta1 + reta2:
    print(f'Os segmentos informados NÃO formam um TRIÂNGULO!')
elif reta1 == reta2 == reta3:
    print('TRIÂNGULO EQUILÁTERO!')
elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
    print('TRIÂNGULO ISÓSCELES!')
else:
    print('TRIÂNGULO ESCALENO!')
