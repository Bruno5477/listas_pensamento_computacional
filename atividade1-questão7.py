#7) Crie um programa que pergunte o nome de um produto e o preço. Ao final ele deve 
#responder o nome e o preço dele com um acréscimo de 10%.
nome = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto:"))
aumento_10 = round(preco * 1.1,2)
print(f"O preço do(a) {nome} com um acréscimo de 10% é de R$ {aumento_10:.2f}") 