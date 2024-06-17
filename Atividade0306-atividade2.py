'''
Questão 2) Dado as senhas abaixo, crie um programa em que se o usuário acertar
uma das senhas,
aparece que acertou a senha.
Caso contrário, pedirá para o usuário digitá-la novamente.
senhas = ['certo', '123', '456']

'''
senhas = ['certo', '123', '456']

while True:

    senha_inserida = input("Digite a senha: ")
 
    if senha_inserida in senhas:
        print("Você acertou a senha!")
        break  
    else:
        print("Senha incorreta, tente novamente.")


