valor_casa = float(input('Digite o Valor da casa: R$')) #le o valor da casa
comprador = float(input('Qual o Salario do Comprador? R$')) #le o salario do comprador
financiamento = int(input('Por quanto tempo deseja pagar o financiamento da casa? ')) #le o tempo de financiamento da casa
#calcula a prestação e o minimo
prestacao = valor_casa / (financiamento * 12)
minimo = comprador * 30 / 100

print('Para pagar uma casa de {:.2f} em {} anos'.format(valor_casa, financiamento), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
#verifica se o emprestimo foi permitido ou negado
if prestacao <= minimo:
    print('Emprestimo Permitido!')
else:
    print('Emprestimo Negado!')