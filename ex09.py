carro = int(input('Quantos Dias você ficou com o carro? '))
km = float(input('Quantos KM rodados? '))
pago_dias = (carro * 60) + (km * 0.15)
print('O total a pagar e de R${:2f}'.format(pago_dias))
