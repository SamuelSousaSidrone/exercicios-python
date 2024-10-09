valor = float(input('Qual o preço do produto que voce deseja comprar? '))
desconto = int(input('Quando o  valor do desconto do seu item? '))

promoçao = (valor * desconto/ 100)

print('O valor original era {}, mas com o desconto de %{}, ficou esse valor {}'.format(valor, desconto, promoçao))