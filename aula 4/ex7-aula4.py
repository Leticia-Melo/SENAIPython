# Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2m2.

altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))

area = largura * altura
litro = area / 2

print('Você precisará de {} litros para pintar sua parede'.format(litro))