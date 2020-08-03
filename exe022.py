nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome maísculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))









