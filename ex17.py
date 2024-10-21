velocidade = int(input('Qual é a Velocidade Atual do Seu Carro? ')) # Velocidade do Carro

limite = 60 #Limite de Velocidade
multa = 150.00 #Multa do Detran

if velocidade <= limite: #Liberado
    print('----------------------------------')
    print('Liberado, Pode Passar')
    print('----------------------------------')
else: # Multado
    print('---------------------------------------------------------------------------------')
    print('Multado, Você Passou o Limite Você tera que pagar uma multa de {}'.format(multa))
    print('---------------------------------------------------------------------------------')