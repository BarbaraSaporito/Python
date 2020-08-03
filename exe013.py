salario = float(input('Qual é o salário do funcionário? '))
aum = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passar a receber {:.2f}'.format(salario, aum))


