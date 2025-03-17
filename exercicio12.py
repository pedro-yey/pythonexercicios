import random

p1 = input('Me fale o primeiro aluno: ')
p2 = input('Me fale o segundo aluno: ')
p3 = input('Me fale o terceiro aluno: ')
p4 = input('Me fale o quarto aluno: ')

lista = [p1, p2, p3, p4]
random.shuffle(lista)  # Embaralha a lista

print('A nova ordem dos alunos é:')
print(lista)  # imprimimos a lista embaralhada corretamente
