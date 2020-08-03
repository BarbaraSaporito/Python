print('\033[32m-=-\033[m' * 5)
print('\033[1;32;46mCalculadora IMC\033[m')
print('\033[32m-=-\033[m' * 5)
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)
print('O seu IMC é de {:.2f}'.format(imc))
if imc <= 16:
    print('Cuidado! Você está no estado de \033[31mMagreza Grave\033[m!')
elif imc <= 18.4:
    print('Cuidado! Você está no estado de \033[31mMagreza Moderada\033[m!')
elif imc <= 25:
    print('Parabéns! Você está no \033[34mPeso ideal\033[m!')
elif imc <= 30:
    print('Atenção! Você está no estado de \033[33mSobrepeso\033[m!')
elif imc <= 35:
    print('Atenção! Você está no estado de \033[31mObesidade nível 1\033[m!')
elif imc <= 40:
    print('Atenção! Você está no estado de \033[31mObesidade severa\033[m!')
else:
    print('Atenção! Você está no estado de \033[31mObesidade mórbida\033[m!')

