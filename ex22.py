salario = float(input('Digite seu Salarío R$: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('O seu Salário novo é {}'.format(novo))