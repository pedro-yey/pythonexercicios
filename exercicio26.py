t1 = float(input('Me fale o primeiro segmento: '))
t2 = float(input('Me fale o segundo segmento: '))
t3 = float(input('Me fale o terceiro segmento: '))

if (t1 + t2 > t3) and (t1 + t3 > t2) and (t2 + t3 > t1):
    print('Dá pra formar um triângulo :D')
else:
    print('Não dá pra formar um triângulo :/')
