# Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF.

# entrada do valor pelo usuário
celsius = float(input('Entre com a temperatura em graus Celsius: '))

#cálculo de ºC para ºF
fahrenheit = 1.8 * celsius + 32   

# exibição do resultado na tela
print(f'{celsius} ºC equivale a {fahrenheit:.2f} ºF.')
