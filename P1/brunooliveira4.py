'''
Questão 4

Faça o somatório dos valores a, b, c e divida por d, sem alterar os dados abaixo. O resultado deverá ser
arredondado para ter apenas uma casa decimal.

'''
a = 15
b = 28.0
c = '110'
d = '50.8'

resultado = (a + b + float(c))/float(d)

print('O resultado é ', round(resultado,1))