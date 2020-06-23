"""
Faça um programa que leia a largura e altura de uma parede em metros, 
calcule a sua área e a quantidade de tintas necessárias para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m².
"""

# inserção dos daos pelo usuário
largura = float(input('Entre com a largura da parede: (m) '))
altura = float(input('Entre com a altura da parede: (m) '))

# cálculo da área total e da quantidade de tinta a ser usada para pintar a parede.
area_total = largura * altura
total_tinta = area_total / 2        

print(f'A parede tem o total de {area_total} m² e é necessário {total_tinta} litros de tinta para pintá-la.')
