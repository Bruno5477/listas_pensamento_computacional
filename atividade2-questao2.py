# Crie um programa que pergunta o numero de vendas para três vendedores.

# vendedor_1 = 700
# vendedor_2 = 1200
# vendedor_3 = 2000

# meta = 100

# Se for abaixo da meta. O salário vai manter o mesmo.

# Se for igual entre 100 a 200, o funcionário receberá 10% em cima do seu salário de bonus.
# se for acima de de 200 o functionário vai receber 40% em cima de seu salário de bonus

vendedor_1 = int(input("Número de vendas do vendedor 1: "))
vendedor_2 = int(input("Número de vendas do vendedor 2: "))
vendedor_3 = int(input("Número de vendas do vendedor 3: "))

if vendedor_1 < 100:
    print("O Número de vendas foi abaixo da meta. O salário do vendedor 1 vai ser de R$ 700.")
elif 100 <= vendedor_1 <= 200 :
    print("O Número de vendas foi dentro da meta. O salário do vendedor 1 foi de R$", round(700*1.1,2))
else:
    print("O número de vendas foi acima da meta. O salário do vendedor 1 foi de R$", round(700*1.4,2))

if vendedor_2 < 100:
    print("O Número de vendas foi abaixo da meta. O salário do vendedor 2 vai ser de R$ 1200.")
elif 100 <= vendedor_2 <= 200 :
    print("O Número de vendas foi dentro da meta. O salário do vendedor 2 foi de R$", round(1200*1.1,2))
else:
    print("O número de vendas foi acima da meta. O salário do vendedor 2 foi de R$", round(1200*1.4,2))

if vendedor_3 < 100:
    print("O Número de vendas foi abaixo da meta. O salário do vendedor 3 vai ser de R$ 2000.")
elif 100 <= vendedor_3 <= 200 :
    print("O Número de vendas foi dentro da meta. O salário do vendedor 3 foi de R$", round(2000*1.1,2))
else:
    print("O número de vendas foi acima da meta. O salário do vendedor 3 foi de R$", round(2000*1.4,2))