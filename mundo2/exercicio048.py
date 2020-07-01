# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for num in range(501):
    if num % 3 == 0:
        if num % 2 == 1:
            soma += num

print(f'A soma de todos os números ímpares de 3 que se encontram no intervalo de 1 a 500 é de: {soma}.')
