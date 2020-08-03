from random import randint
from time import sleep
pc = randint(0,5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 18)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if num == pc:
    print('Parabéns você conseguiu adivinhar!')
else:
    print('Errou! Eu pensei no número {}'.format(pc))

