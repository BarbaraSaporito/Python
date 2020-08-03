maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {:.1f} kg'.format(menor))
print('O maior peso é {:.1f} kg'.format(maior))