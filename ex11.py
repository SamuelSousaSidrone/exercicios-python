import random

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O escolhido foi', escolhido)