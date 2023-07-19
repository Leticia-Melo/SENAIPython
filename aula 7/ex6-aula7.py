num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

max = num1
min = num3

if num2 > max:
    max = num2
if num3 > max:
    max = num3

if num1 < min:
    min = num1
if num2 < min:
    min = num2
print('O menor número é: {}\nE o maior número é: {}'.format(min,max))