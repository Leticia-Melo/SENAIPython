import random
joke = input('Digite Pedra, Papel ou Tesoura:\n').lower()
a = 'pedra', 'papel', 'tesoura'
pc = random.choice(a)

if pc==joke:
    print(pc)
    print('Empate!')
elif joke == 'pedra' and pc == 'tesoura':
    print(pc)
    print('Você venceu')
elif joke == 'pedra' and pc == 'papel':
    print(pc)
    print('Você perdeu!')
elif joke == 'papel' and pc == 'pedra':
    print(pc)
    print('Você venceu')
elif joke == 'papel' and pc == 'tesoura':
    print(pc)
    print('Você perdeu')
elif joke == 'tesoura' and pc == 'pedra':
    print(pc)
    print('Você perdeu!')
elif joke == 'tesoura' and pc == 'papel':
    print(pc)
    print('Você venceu')
else:
    print('Digite um valor válido')