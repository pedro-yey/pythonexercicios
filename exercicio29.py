#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('Me fale um número inteiro: '))
n2 = int(input('Me fale outro número inteiro: '))

if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n2 > n1:
    print('O SEGUNDO número é maior.')
else:
    print('Os números são equivalentes.')
