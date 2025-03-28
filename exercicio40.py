#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tabuada=int(input('Me fale um número inteiro: '))
for i in range(0,11):
    print('{} x {} = {}'.format(tabuada,i, tabuada*i))