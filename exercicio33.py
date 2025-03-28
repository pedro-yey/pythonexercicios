
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Os segmentos acima PODEM formar um triângulo ")


    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo.")
