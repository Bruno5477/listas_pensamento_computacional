'''
Questão 5) Crie um programa que solicita do usuário a quantidade de
dígitos. Posteriormente, deverá aparecer uma senha aleatória com a
quantidade de dígitos numéricos inseridos
'''

import random

num_digitos = int(input('Insira o número de dígitos da senha:'))
senha = ''.join(random.choice('0123456789') for _ in range(num_digitos))

print(f"A senha gerada é: {senha}")
