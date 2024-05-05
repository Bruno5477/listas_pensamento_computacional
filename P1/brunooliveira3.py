'''
Questão 3

Crie um programa que, pergunte ao usuário se ele está bem.
O usuário deverá responder sim ou não com: (sim/nao)
Se a resposta for sim , responda: Que bom!
Se ele responder nao , pergunte: Por qual motivo?
Independente da resposta, deverá responder: Lamento!
'''

user = input('Você está bem? ')

if user == 'sim':
    print('Que bom!')
elif user == 'nao':
    input('Por qual motivo ?')
    print('Lamento!')