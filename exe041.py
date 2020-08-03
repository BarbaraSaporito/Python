from datetime import date

print('\033[37m-=-\033[m' * 7)
print('\033[31mCATEGORIA DO ATLETA\033[m')
print('\033[37m-=-\033[m' * 7)

nasc = int(input('Qual o ano do seu nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: \033[36mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[35mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[34mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[33mSÊNIOR\033[m')
else:
    print('Classificação: \033[32mMASTER\033[m')

