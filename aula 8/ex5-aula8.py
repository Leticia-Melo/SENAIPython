from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é Mirim')
if 10 <= idade <= 14:
    print('Sua categoria é Infantil')
if 15 <= idade <= 19:
    print('Sua categoria é Júnior')
if idade==20:
    print('Sua categoria é Sênior')
if idade>=21:
    print('Sua categoria é Master')
