"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'O seu IMC é: {imc:.1f}. \nVocê está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'O seu IMC é: {imc:.1f}. \nVocê está no PESO IDEAL!')
elif 25 <= imc < 30:
    print(f'O seu IMC é: {imc:.1f}. \nVocê está com SOBREPESO!')
elif 30 <= imc < 40:
    print(f'O seu IMC é: {imc:.1f}. \nVocê está com OBESIDADE!')
else:
    print(f'O seu IMC é: {imc:.1f}. \nVocê está com OBESIDADE MÓRBIDA!')
