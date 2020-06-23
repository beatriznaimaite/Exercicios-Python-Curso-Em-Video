# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘SANTO’.

# inserção dos dados pelo usuário
cidade = str(input('Digite o nome da cidade: ')).strip().upper()

# tratamento de string
separacao_cidade = cidade.split()

# teste lógico
if 'SANTOS' in separacao_cidade[0] or not 'SANTO' in separacao_cidade[0]:
    print('Não comeca com SANTO')
elif 'SANTO' in separacao_cidade[0]:
    print('Começa com SANTO')
