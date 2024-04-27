# Crie um programa onde o usuário digita um numero. Se for par, será informado
# que é par. Se for impar, será informado que é impar

num = int(input("Insira um número inteiro: "))

if (num % 2) == 0:
    print("O número par")
else:
    print("O Número é ímpar")