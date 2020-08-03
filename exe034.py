salario = int(input('Qual o valor do seu salário: '))
if salario <= 1250:
    aum = (15 * salario / 100) + salario
else:
    aum = (10 * salario / 100) + salario
print('Seu novo salário com aumento é de \033[7;31;40mR${:.2f}\033[m'.format(aum))
