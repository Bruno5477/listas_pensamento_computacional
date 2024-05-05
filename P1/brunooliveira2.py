'''
Questão 2

Um atacadista quer inserir um desconto de 40% em todos os produtos em uma promoção relampago! Crie
um programa onde o usuário digita o nome de um produto e o seu preço. Ao Lnal será mostrado a
mensagem informando:
Exemplo: A bola vai custar 16 reais com 40% de desconto

'''

produto = input('Insira o nome do produto: ')
valor = float(input('Agora informe o preço do produto: '))

valor_final = valor -(valor*.4)

print(f'O {produto} vai custar R$ {valor_final} com 40% de desconto.')