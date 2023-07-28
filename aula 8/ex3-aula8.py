# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, uma das mensagens:
# ▪ Se ele ainda vai se alistar no serviço militar
# ▪ Se é hora de se alistar
# ▪ Se já passou do tempo de alistamento
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano

if idade == 18:
    print('É hora de se alistar')
elif idade > 18:
    print('Já passou da hora de se alistar')
    passou = idade - 18
    print('Passou {} anos do prazo'.format(passou))
elif ano > date.today().year:
    print('Valor inválido!')
else:
    print('Ainda irá se alistar')
    falta = 18 - idade
    print('Ainda faltam {} anos'.format(falta))