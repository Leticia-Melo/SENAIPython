import random
num2 = int(input('Tente adivinhar o número: '))

pc = random.randint(0,5)

print(pc)
print('Acertou' if num2==pc else 'Errou')