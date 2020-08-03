num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}...'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

num = str(input('Digite um número de quatro digitos:'))
print('A sua unidade é: {}'.format(num[4]))
print('A sua dezena é: {}'.format(num[3]))
print('A sua centena é: {}'.format(num[2]))
print('E seu milhar é: {}'.format(num[1]))


