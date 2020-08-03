lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
tinta = area/2
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m². '
      '\nPara pintar essa parede, você precisará de {} litros de tinta'.format(lar, alt, area, tinta))







