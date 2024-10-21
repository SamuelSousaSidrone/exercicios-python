ano = int(input('Qual ano você quer analisar? ')) # pede o ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #verifica se e bissexto ou não
    print('O ano {} é bissexto'.format(ano))
else:
    print('Esse ano {} não e bissexto'.format(ano))
