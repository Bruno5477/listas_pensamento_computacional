# Crie um programa onde o usuário digita nota de P1 e P2, 
# Se a nota for maior ou igual a 7, ele está aprovado.
# Se for abaixo, está reprovado

p1 = float(input("Qual a nota da p1? "))
p2 = float(input("Qual a nota da p2? "))
media = (p1 + p2)/2

if media >= 7 :
    print("Parabéns, você foi aprovado!")
else:
    print("Que pena, você foi reprovado.")