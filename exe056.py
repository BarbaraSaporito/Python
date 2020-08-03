sidade = 0
midade = 0
maiorhomem = 0
nomevelho = 0
maior20 = 0

for d in range(1, 5):
    print('----- {}ª PESSOA ------'.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    sidade += idade
    if d == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        maior20 += 1

midade = sidade / d
print('A média de idade do grupo é {} anos'.format(midade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(maior20))