#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Qual velocidade você estava? "))

if velocidade <= 80:
    print("Tudo certo!")
else:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"Você passou da velocidade permitida e será multado!")
    print(f"O valor da multa é de R${multa:.2f}.")