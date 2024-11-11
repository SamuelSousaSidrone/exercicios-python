print('Digite 3 Valores')
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

menor = a
maior = c
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

if b>a and b>c:
    maior = b
if a>c and a>b:
    maior = a

print('---------------------------------------')
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))