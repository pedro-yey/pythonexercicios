#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
peso=float(input('Bem vindo ao cálculo de IMC! Me fale o seu peso em kg: '))
altura=float(input('Me fale a sua altura: '))
IMC=peso/(altura*2)
if IMC<18.5:
    print('O seu IMC é {:.1f}! Está abaixo da média!'.format(IMC))
elif IMC<25:
    print('O seu IMC é {:.1f}! Está no peso ideal!'.format(IMC))
elif IMC<=30:
    print('O seu IMC é {:.1f}! Está Sobrepeso! '.format(IMC))
elif IMC<=40:
    print('O seu IMC é {:.1f}! Está Obeso!'.format(IMC))
else:
    print('O seu IMC é {:.1f}! Está com uma Obesidade Mórbida.'.format(IMC))