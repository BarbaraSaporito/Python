num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {}{}{} é par'.format('\033[1;34m', num, '\033[m'))
else:
    print('O número {}{}{} é ímpar'.format('\033[1;34m', num, '\033[m'))

