print('\033[31m-=-\033[m' * 10)
print('\033[37mANALISADOR DE TRIÂNGULOS 2.0\033[m')
print('\033[31m-=-\033[m' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima \033[1;34mPODEM\033[m formar um triângulo', end=' ')
    if a == b and b == c:
        print('\033[35mEQUILÁTERO.\033[m')
    elif a != b and a != c and b != c:
        print('\033[32mESCALENO.\033[m')
    else:
        print('\033[33mISÓSCELES.\033[m')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo')





