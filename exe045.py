from random import randint
from time import sleep
pc = randint(0,2)
itens = ('\033[35mPEDRA\033[m', '\033[33mPAPEL\033[m', '\033[36mTESOURA\033[m')
print('\033[1;31m{:=^30}\033[m'.format('JOKENPÔ'))
print('''ESCOLHA UMA OPÇÃO: 
[0] \033[35mPEDRA\033[m
[1] \033[33mPAPEL\033[m
[2] \033[36mTESOURA\033[m''')
jogada = int(input('Qual sua jogada: '))
print('JÓ...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔÔÔ!!!')
print('-=-' * 10)
print('O computador escolheu {}'.format(itens[pc]))
print('Jogador escolheu {}'.format(itens[jogada]))
print('-=-' * 10)
if pc == 0: # pc jogou pedra
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('JOGADOR VENCEU!')
    elif jogada == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif pc == 1: #pc jogou papel
    if jogada == 0:
        print('COMPUTADOR VENCEU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('JOGADOR VENCEU!')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif pc == 2: #pc jogou tesoura
    if jogada == 0:
        print('JOGADOR VENCEU!')
    elif jogada == 1:
        print('COMPUTADOR VENCEU!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')




