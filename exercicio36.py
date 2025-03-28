import random

opcoes = ['pedra', 'papel', 'tesoura']

print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

escolha_usuario = input("Digite sua escolha (1, 2 ou 3): ")

if escolha_usuario not in ['1', '2', '3']:
    print("Escolha inválida. Tente novamente!")
else:
    escolha_usuario = opcoes[int(escolha_usuario) - 1]
    escolha_computador = random.choice(opcoes)

    print(f"\nVocê escolheu {escolha_usuario}.")
    print(f"O computador escolheu {escolha_computador}.\n")

    if escolha_usuario == escolha_computador:
        print("É um EMPATE!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você GANHOU!")
    else:
        print("Você PERDEU!")
