# 1) Crie um programa que fale olá, mundo!
print("Olá, mundo!")

#2) Crie um programa que realize a soma dos três produtos do mercado do Jon e imprima o resultado.

coca = 8.50
pizza = 12.00
pudim = 10.75

soma = coca + pizza + pudim
print("A soma dos 3 produto é igual a", soma)

#3) Você fez duas provas. p1 e p2. Você precisa descobrir qual a sua média. Crie um programa
# o qual você insere a sua nota e ao final, irá fornecer o resultado dessa média.

p1 = 10
p2 = 8
media = p1 + p2

print("A média das notas é:", media)

# 4) Crie um programa que calcule seu IMC (indice de massa corpórea). Lembrando que para
#elevar um número ao quadrado, usa o **
peso = 82
altura = 1.75

imc = peso / altura**2

print("O valor do imc é igual a:", round(imc,3)) # usei o round para arredondar o valor até 3 casas decimais.

#5) Faça a multiplicação a seguir, convertendo o valor2 que é uma string em inteiro (int):
valor1 = 5
valor2 = '3'

multiplicacao = valor1 * int(valor2)

print("O valor da multiplicação é igual a:", multiplicacao)

#6) Utilze type para informar qual é o tipo das variáveis a seguir:

nome = 'Ciclano'
idade = 39
peso = 90.55

print("A variável nome é do tipo", type(nome))
print("A variável idade é do tipo", type(idade))
print("A variável peso é do tipo", type(peso))

#7) Crie um programa que pergunte o nome de um produto e o preço. Ao final ele deve 
#responder o nome e o preço dele com um acréscimo de 10%.
nome = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto:"))
acres_10 = round(preco * 1.1,2)
print("O preço do(a)", nome, "com um acréscimo de 10% é de R$",acres_10)

#8) Crie um programa que calcule quantos anos, faltam para você completar 100 anos de idade.

idade = int(input("Digite sua idade em anos completos:"))
idade_100 = 100 - idade
print("Faltam", idade_100, "anos para você completar 100 anos de idade")
