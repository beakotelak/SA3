ced = 100.00
numced = 0
valor = float(input('Valor da compra R$: '))
pag = float(input('Pagamento R$: '))
troco = pag - valor
total = troco

if pag < valor:
    print('\n O valor pago pelo cliente não é suficiente para completar compra.')
elif pag == valor:
    print('\n Troco ao cliente é de R$ 0,00. \n Pagamento concluído!')
else:
    print('\n O troco é R$ {:.2f}\n'.format(troco))
    while True:
        if total >= ced:
            total -= ced
            numced += 1
        else:
            if numced > 0:
                if ced > 1:
                    print('{} cédula(s) de R${:.2f}'.format(numced, ced))
                if ced <= 1:
                    print('{} moeda(s) de R${:.2f}'.format(numced, ced))
            if ced == 100.00:
                ced = 50.00
            elif ced == 50.00:
                ced = 20.00
            elif ced == 20.00:
                ced = 10.00
            elif ced == 10.00:
                ced = 5.00
            elif ced == 5.00:
                ced = 2.00
            elif ced == 2.00:
                ced = 1.00
            elif ced == 1.00:
                ced = 0.50
            elif ced == 0.50:
                ced = 0.25
            elif ced == 0.25:
                ced = 0.10
            elif ced == 0.10:
                ced = 0.05
            elif ced == 0.05:
                ced = 0
            numced = 0
            if total == 0:
                break
    print('\nPagamento concluído!')