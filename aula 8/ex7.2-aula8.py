# Escreva um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# ▪ À vista (dinheiro ou cheque): 10% de desconto
# ▪ À vista no cartão: 5% de desconto
# ▪ Em até 2x no cartão: preço normal
# ▪ 3x ou mais no cartão: 20% de juros

# Realizei uma versão onde não seria preciso digitar sim ou não, apenas
# 1 e 2 com legendas nos input e quantas vezes iria parcelar o valor.

prod = float(input('Digite o valor do produto: R$'))
car = int(input('O pagamento será no cartão?\n1= Sim 2= Não\n'))

if car==1:
    vis = int(input('O valor será à vista?\n1= Sim 2= Não\n'))
    if vis==1:
        val = car - (car*0.5)
        print('O valor do produto será R${:.3f}'.format(val))
    if vis==2:
        parc = int(input('O valor será em até quantas vezes? '))
        if parc ==2:
            val = prod / 2
            print('O valor do produto será R${:.3f} por mês'.format(val))
        elif parc >=3:
            print('O pagamento então será em até 3x ou mais!')
            val = prod + (prod*0.20)
            val2 = val / parc
            print('Você irá pagar R${:.3f} por mês'.format(val2))
elif car==2:
    print('O pagamento então será no dinheiro ou cheque!')
    din = prod - (prod*0.10)
    print('O valor do produto será R${:.3f}'.format(din))