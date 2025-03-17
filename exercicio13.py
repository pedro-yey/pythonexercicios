nome=input('Digite seu nome completo')
print('analisando...')
print ('Seu nome completo em Maiúsculo é', nome.upper())
print('Seu nome completo em Minúsculo é', nome.lower())
print(len(nome.replace(' ', '')))
primeiro_nome = nome.split()[0]  
print("Número de letras no primeiro nome:", len(primeiro_nome))
