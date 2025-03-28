ano=int(input('Quantos anos você tem? '))
if ano<9:
    print('Você é da categoria Mirim!')
elif ano<=15:
    print('Você é da categoria Infantil!')
elif ano<=19:
    print('Você é da categoria dos Juniores!')
elif ano<=25:
    print('Você é um sênior!')
else:
    print('Você é Master!')
