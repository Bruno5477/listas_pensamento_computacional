'''
Questão 3) Crie um programa onde o usuário irá digitar:
o nome, idade salário e sexo biológico (m/f).
O usuário vai precisar digitar um nome com mais de 2 letras,
caso tenha menos, deverá solicitar novamente o nome.
O salário precisa ser um valor positivo,
se não, deverá solicitar novamente.
O sexo, deverá ser m ou f, se não, irá solicitar novamente.

'''

def name():
    while True:
        nome = input("Digite seu nome (mais de 2 letras): ")
        if len(nome) > 2:
            return nome
        else:
            print("Nome inválido. Por favor, digite um nome com mais de 2 letras.")

def age():
    while True:
        try:
            idade = abs(int(input("Digite sua idade: ")))
            return idade
        except ValueError:
            print("Idade inválida. Por favor, digite um número inteiro.")

def salary():
    while True:
        try:
            salario = float(input("Digite seu salário (valor positivo): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. Por favor, digite um valor positivo.")
        except ValueError:
            print("Salário inválido. Por favor, digite um número.")

def birth_gender():
    while True:
        sexo = input("Digite seu sexo biológico (m/f): ").lower()
        if sexo in ['m', 'f']:
            return sexo
        else:
            print("Sexo inválido. Por favor, digite 'm' para masculino ou 'f' para feminino.")


nome = name()
idade = age()
salario = salary()
sexo = birth_gender()

print("\nInformações coletadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo biológico: {'Masculino' if sexo == 'm' else 'Feminino'}")

