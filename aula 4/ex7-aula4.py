altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))

area = largura * altura
litro = area / 2

print('Você precisará de {} litros para pintar sua parede'.format(litro))