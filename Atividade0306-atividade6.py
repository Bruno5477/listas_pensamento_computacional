'''
Questão 6) Agora, crie um programa que o usuário deverá informar
quantidade de letras, caracteres (como $, #, @, &...) e números e será
fornecido uma senha aleatória.
Exemplo:
senha: aA$6$123k
'''
import random
import string

letras = string.ascii_letters
numeros = string.digits
caracteres = string.punctuation

# Seu código abaixo

n_letras = int(input('Digite o número de letras: '))
n_numeros = int(input('Digite o número de números: '))
n_caracteres = int(input('Digite o número de caracteres especiais:'))
senha = []

for i in range(n_letras):
    senha.append(random.choice(letras))

for i in range(n_numeros):
    senha.append(random.choice(numeros))

for i in range(n_caracteres):
    senha.append(random.choice(caracteres))

senha = ''.join(senha)
print(senha)