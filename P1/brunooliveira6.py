'''
Questão 6

Em um sistema de aprovação da Universidade Exemplo,
Crie um programa o qual o professor digita a nota do aluno de P1 (primeira prova) e P2
(segunda prova) e fornece a média.
Se a média for igual ou maior que 7, o aluno estará aprovado.
Se for abaixo de 7, não estará aprovado.
Se essa nota de não aprovação for maior ou igual a 3, ele terá uma nova chance, para fazer
uma prova final (P3). A nota abaixo de 3, estará reprovado.
Nessa prova final (p3), é desconsiderado todas as notas anteriores da matéria e o aluno
deverá tirar uma nota maior ou igual a 6 para ser aprovado.
Caso ele ainda não consiga tirar a nota de aprovação na P3 e não tenha tirado uma nota
abaixo ou igual a 3 (que reprovaria na P3), ele poderá fazer uma prova que se chama
Segunda época que é a última chance!
Nessa prova segunda época, o aluno deverá tirar nota maior ou igual a 6 para que seja
aprovado. Se tirar abaixo, estará reprovado!
'''

p1 = float(input('Insira a nota da primeira prova: '))
p2 = float(input('Insira a nota da segunda prova: '))

media = (p1 + p2)/2

if media >= 7:
    print(f'Parabéns sua média foi {media}, você está aprovado!')
elif media >= 3 and media < 7:
    p3 = float(input('Insira a nota da sua terceira prova: '))
    if p3 >= 6:
        print(f'Parabéns sua nota foi {p3}, você está aprovado!')
    elif p3 >= 3 and p3 < 6:   
        se = float(input('Insira a nota da sua segunda época: ')) 
        if se >= 6:
            print(f'Parabéns sua nota na segunda época foi {se}, você está aprovado!')
        else:
            print(f'Sua nota na segunda época foi {se}, você está reprovado.')
else:
    print(f'Sua nota foi {media}, você não foi aprovado')
    
