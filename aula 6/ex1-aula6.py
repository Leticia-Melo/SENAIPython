nome = input('Digite seu nome completo: ')

maius = nome.upper()

minus = nome.lower()

letras = len(nome)-nome.count(' ')

contagem = nome.split()[0]
prim_nome = len(contagem)

print('Seu nome em maiúsculo é: {}'.format(maius))
print('Seu nome em minúsculo é: {}'.format(minus))
print('Seu nome tem: {} letras'.format(letras))
print('Seu primeiro nome tem: {} letras'.format(prim_nome))