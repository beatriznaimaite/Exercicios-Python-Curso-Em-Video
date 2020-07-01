"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

idade = totM20 = H_mais_velho_idade = 0
for p in range(1, 5):
    nome = str(input('Digite o nome: ')).strip().capitalize()
    anos = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('-----------------------------------')
    idade += anos

    if anos < 20 and sexo == 'F' :
        totM20 += 1

    if sexo == 'M':
        if p == 1:
            H_mais_velho_idade = anos
            homem_velho_nome = nome
        else:
            if anos > H_mais_velho_idade:
                H_mais_velho_idade = anos
                homem_velho_nome = nome  

media = idade/4

print(f'A média de idade foi de {media:.1f} anos.')
print(f'Ao todo, tem {totM20} mulher(es) com menos de 20 anos.')
print(f'O homem mais velho cadastrado foi o {homem_velho_nome} e ele tem {H_mais_velho_idade} anos.')
