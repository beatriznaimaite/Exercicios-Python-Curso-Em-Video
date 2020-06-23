"""
Escreva um programa que leia a velocidade de uma carro. 
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$ 7,00 por cada Km acima do limite. 
"""

# inserção da velocidade
velocidade = input('Digite a velocidade do carro (km/h): ')
velocidade = float(velocidade.replace(',','.'))

# teste lógico
if velocidade > 80:
    excedido = velocidade - 80
    multa = excedido * 7
    print(f'Você excedeu o limite em {excedido} km! Sua multa será no valor de R$ {multa:.2f}.')
else:
    print('Você está dentro do limite de velocidade!')
