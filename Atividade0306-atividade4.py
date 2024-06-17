'''
Questão 4) Assim como o primeiro exercício, o usuário irá digitar uma
senha, se for uma senha certa, deverá aparecer a mensagem de senha
correta. Se for errada, o usuário digitar novamente. No entanto, se for
errado 3 vezes, irá aparecer a mensagem de senha bloqueada.
'''
senhas = ['certo', '123', '456']

tentativas = 3


while tentativas > 0:
    senha_inserida = input("Digite a senha: ")


    if senha_inserida in senhas:
        print("Senha correta!")
        break  
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Senha incorreta, tente novamente.")

if tentativas == 0:
    print("Senha bloqueada.")