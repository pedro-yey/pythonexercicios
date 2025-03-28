#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input("Quantos quilômetros você vai percorrer? "))

if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45

print("O custo da viagem será R${:.2f}".format(preco))



