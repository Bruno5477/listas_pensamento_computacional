'''
Crie um programa que:
Dado um inteiro, realize as seguintes ações condicionais:
Se  for ímpar, imprima Estranho
Se  for par e estiver no intervalo inclusivo de 2 a 5, imprima Não Estranho
Se  for par e estiver no intervalo inclusivo de 6 a 20, imprima Estranho
Se  for par e maior que 20, imprima Não Estranho
'''
number = int(input("Insira um número inteiro: "))

if number % 2 !=0:
    print(f'{number} Estranho.')
elif 2 <= number <= 5:
    print(f'{number} Não Estranho')
elif 6 <= number <= 20:
    print(f'{number} Estranho')
else:
    print(f'{number} Não Estranho')