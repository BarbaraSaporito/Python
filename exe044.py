print('{:=^40}'.format('\033[1;31mLojas Saporito\033[m'))
total = float(input('Valor total em compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    final = total - (total * 10 /100)
elif opcao == 2:
    final = total - (total * 5 /100)
elif opcao == 3:
    final = total
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(total/2))
elif opcao == 4:
    final = total + (total * 20 / 100)
    parcela = int(input('Qual total de parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcela, final/parcela))
else:
    final = total
    print('\033[31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(total, final))
