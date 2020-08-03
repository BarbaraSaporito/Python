from datetime import date

print('\033[35m-=-\033[m' * 7)
print('\033[36mAlistamento militar\033[m')
print('\033[35m-=-\033[m' * 7)

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
alistamento = ano + 18

if idade < 18:
    print('Quem nasceu em em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em: {}'.format(alistamento))
elif idade > 18:
    print('Quem nasceu em em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
    print('Você já deveria ter se alistado há {} anos'.format(date.today().year - alistamento))
    print('Seu alistamento foi em: {}'.format(alistamento))
else:
    print('Quem nasceu em em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
    print('Você tem que se alistar imediatamente')






