import random
aluno1 = input('Qual o Nome do Primeiro Aluno: ')
aluno2 = input('Qual o Nome do Segundo Aluno: ')
aluno3 = input('Qual o Nome do Terceiro Aluno: ')
aluno4 = input('Qual o Nome do Quarto Aluno: ')
aluno5 = input('Qual o Nome do Quinto Aluno: ')

lista = [aluno1 , aluno2, aluno3, aluno4, aluno5]

random.shuffle(lista) #embarralha a lista

print('A ordem sera: ')
print(lista)