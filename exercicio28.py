#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))


print('Escolha a base de conversão:')
print('1 - Para Binário')
print('2 - Para Octal')
print('3 - Para Hexadecimal')
opcao = int(input("Sua opção: "))


if opcao == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:].upper()}')
else:
    print("Opção inválida. Escolha 1, 2 ou 3.")
