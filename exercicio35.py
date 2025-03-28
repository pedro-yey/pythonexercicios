#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
valor = float(input('Valor do Pagamento: R$ '))

print('FORMAS DE PAGAMENTO:')
print('[1] - À vista dinheiro/cheque (10% de desconto)')
print('[2] - À vista no cartão (5% de desconto)')
print('[3] - Em até 2x no cartão (preço normal)')
print('[4] - 3x ou mais no cartão (20% de juros)')

formas = int(input('Escolha uma opção: '))

if formas == 1:
    total = valor * 0.90
    print(f'O novo valor será de R$ {total:.2f}')

elif formas == 2:
    total = valor * 0.95
    print(f'O valor à vista no cartão será de R$ {total:.2f}')

elif formas == 3:
    parcela = valor / 2
    print(f'Pagamento parcelado em 2x de R$ {parcela:.2f}')
    print(f'Total a pagar: R$ {valor:.2f}')

elif formas == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        total = valor * 1.20
        parcela = total / parcelas
        print(f'Pagamento parcelado em {parcelas}x de R$ {parcela:.2f}')
        print(f'Total a pagar: R$ {total:.2f}')
    else:
        print('Erro! Escolha pelo menos 3 parcelas.')

else:
    print('Opção inválida! Escolha entre 1 e 4.')



