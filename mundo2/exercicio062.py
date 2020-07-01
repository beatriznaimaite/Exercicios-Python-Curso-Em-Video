"""
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primeiro_termo = int(input('Digite o primeiro termo de uma P.A.: '))
razao = int(input('Digite a razao dessa P.A.: '))
termos = int(input('Quantos termos você quer mostrar? '))

mais = cont = 0
while cont < termos:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    cont += 1

    while cont == termos:
        perg = str(input('\nQuer mostrar mais termos? [S/N]: ')).strip().upper()[0]

        while perg not in 'SN':
            perg = str(input('\nQuer mostrar mais termos? [S/N]: ')).strip().upper()[0]
        if perg == 'N':
            print('FINALIZANDO...')
            break                     
        if perg == 'S':
            termos = int(input('Quantos termos a mais você quer mostrar? '))
            cont = 0
            if termos == 0:
                print(f'Você digitou o número zero, finalizando...')
                break
