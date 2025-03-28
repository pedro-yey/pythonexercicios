#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
nasc=int(input('Ano de Nascimento: '))
idade= ano_atual - nasc
print('Você nasceu no ano de {} e você tem {} em {}'.format(nasc,idade,ano_atual))
if idade==18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade>18:
    print('Você não precisa se alistar, você se alistou há {} anos.'.format(idade-18))
else:
    print('Você irá se alistar daqui há {} anos'.format(18-idade))

