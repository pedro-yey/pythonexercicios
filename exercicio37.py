##Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time

for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)

print("💥 BOOM! Feliz Ano Novo! 🎆")