# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

dado = input('Digite qualquer coisa: ')

print('O dado que você digitou é do tipo primitivo', type(dado),
      '\nSó tem números?', dado.isnumeric(),
      '\nÉ alfanumérico?', dado.isalpha(),
      '\nSó tem espaços?', dado.isspace(),
      '\nEstá tudo em minúsculo?', dado.islower(),
      '\nEstá tudo em maiúsculo?', dado.isupper(),
      '\nTem letras maiúsculas e minúsculas?', dado.istitle())
