num = int(input('Digite um número inteiro: '))
print('-=-' * 13)
print('''Escolha uma das bases para conversão: 

\033[1;31m[1]\033[m converter para \033[35mBINÁRIO\033[m
\033[1;31m[2]\033[m converter para \033[36mOCTAL\033[m
\033[1;31m[3]\033[m converter para \033[34mHEXADECIMAL\033[m''')
print('-=-' * 13)
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em \033[35mBINÁRIO\033[m é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em \033[36mOCTAL\033[m é {}'.format(num, oct(num)[:2]))
elif opcao == 3:
    print('O número {} em \033[34mHEXADECIMAL\033[m é {}'.format(num, hex(num)[2:]))
else:
    print('''\033[1;31mOpção inválida. 
TENTE NOVAMENTE:\033[m
Escolha uma das bases para conversão: 

\033[1;31m[1]\033[m converter para \033[35mBINÁRIO\033[m
\033[1;31m[2]\033[m converter para \033[36mOCTAL\033[m
\033[1;31m[3]\033[m converter para \033[34mHEXADECIMAL\033[m  ''')

