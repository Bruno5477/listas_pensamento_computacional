'''
Questão 5) Crie um programa que solicita do usuário a quantidade de
dígitos. Posteriormente, deverá aparecer uma senha aleatória com a
quantidade de dígitos numéricos inseridos
'''

import random
import string

numeros = string.digits 
letras = string.ascii_letters
caracteres = string.punctuation

num_digitos = int(input('Insira o número de dígitos da senha:'))
senha = ''.join(random.choice(numeros,letras, caracteres) for _ in range(num_digitos))

print(f"A senha gerada é: {senha}")
