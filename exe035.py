print('-=-' * 9)
print('Analisador de triângulos')
print('-=-' * 9)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima \033[1;34mPODEM\033[m formar um triângulo')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo')

