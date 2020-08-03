dia = int(input('Quantos dias de aluguel do veículo? '))
km = float(input('Quantos quilometros rodados? '))
total = (dia * 60) + (km * 0.15)
print('O total a pagar é {:.2f}'.format(total))



