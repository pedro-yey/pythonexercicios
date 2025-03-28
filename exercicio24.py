#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input('Me fale seu salário '))
if (salario)<=1250.00:
    salario2=salario * 0.15
    salario4=salario + salario2
    print('O valor de seu novo salário é {} R$.'.format(salario4))
else:
    salario3=salario * 0.10
    salario5=salario+salario3
    print('O valor de seu novo salário é {} R$.'.format(salario5))