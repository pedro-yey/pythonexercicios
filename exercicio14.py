num = int(input("Digite um número entre 0 e 9999: "))

num_str = "{:04d}".format(num)

print("Unidade: {}".format(num_str[3]))
print("Dezena: {}".format(num_str[2]))
print("Centena: {}".format(num_str[1]))
print("Milhar: {}".format(num_str[0]))
