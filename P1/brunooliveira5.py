'''
Questão 5

A loja Python Toys muda seus preços de acordo com alguns eventos.
Crie um programa que o qual o vendedor informa o preço de um produto. Posteriormente, ele deve
perguntar se é uma data festiva.
Caso positivo, insira um acréscimo de 45%.
Caso negativo, mantenha o preço normal. Caso seja Black Friday, insira um desconto de 30% no preço
final

'''

preco = float(input('Insira o preço do produto: '))

data_festiva = input('É data festiva ? \nsim: \nnao:\n')

if data_festiva == 'sim':
    print(f'O preço final do produto é de R$ {preco*1.4}')    
else:
    black = input('É Black Friday? \nsim: \nnao:\n')
    if black == 'sim':
        print(f'O preço final do produto é de R$ {preco*0.7}')
    else:
        print(f'O preço final do produto é de R$ {preco}')


   


