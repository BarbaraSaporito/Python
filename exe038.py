print('\033[35m-=-\033[m' * 16)
print('\033[36mEscolha dois números e vou dizer qual é o maior\033[m')
print('\033[35m-=-\033[m' * 16)
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O \033[33mPRIMEIRO\033[m valor é maior!')
elif num2 > num1:
    print('O \033[33mSEGUNDO\033[m valor é maior!')
else:
    print('Os \033[33mDOIS\033[m números são iguais!')
