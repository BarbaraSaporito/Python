from datetime import date
ano = int(input('Qual ano deseja analisar? Digie 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 1 or ano % 400 == 0:
    print('O ano {} \033[35mÉ\033[m bissexto'.format(ano))
else:
    print('O ano {} \033[31mNÃO\033[m é bissexto'.format(ano))




