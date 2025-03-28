nota1=float(input('Me fale a primeira nota '))
nota2=float(input('Me fale a segunda nota '))
media=(nota1+nota2)/2
if media >=7:
    print('Parabéns! Você está aprovado.')
elif media<5:
    print('Infelizmente você reprovou!')
elif 7>media >=5:
    print('Você está na recuperação!')
