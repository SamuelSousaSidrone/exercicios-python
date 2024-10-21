from random import randint

computador = randint(0, 5) # Numero "Aleatorio" da Maquina

print('-----------------------------------')
print('Pensei em um numero entre 0 e 5, Tente Adivinhar')
print('-----------------------------------')

jogador = int(input('Em qual numero eu pensei? ')) # Jogador Adivinha 

if jogador == computador:
    print('Parabens Você Acertou o Numero!')
else:
    print('Você Errou, Mais Sorte na Proxima, eu tinha pensado no Numero {}'.format(computador))

#Finalizado 