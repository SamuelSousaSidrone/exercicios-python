numero = float(input("Digite seu Valor em Reais para converter: "))

dolar = numero / 5.45
euro = numero / 6.03

print('O seu Valor e R${}, o seu Valor em Dolar e US {} e em Euro e EUR {}'.format(numero, dolar, euro))