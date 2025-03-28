#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa=float(input('Qual o valor da Casa? '))
salario=float(input('Qual o seu salário? '))
anos=float(input('Em quantos anos de financiamento? '))
meses=anos * 12
prestacao=casa/meses
limite=salario * 0.3
if (prestacao)>=limite:
    print('Empréstimo negado.')
elif (limite)>=prestacao:
    print('Empréstimo aprovado!')
