prod = float(input('Digite o valor do produto: R$'))
car = input('O pagamento será no cartão? ').upper()

if car=='SIM':
    vis = input('O valor será à vista? ').upper()
    if vis=='SIM':
        val = car - (car*0.5)
        print('O valor do produto será R${:.3f}'.format(val))
    if vis=='NÃO':
        vis = input('O valor será em até 2x? ').upper()
        if vis == 'SIM':
            val = prod / 2
            print('O valor do produto será R${:.3f} por mês'.format(val))
        if vis == 'NÃO':
            print('O pagamento então será em até 3x ou mais!')
            par = int(input('Em quantas vezes você irá parcelar? '))
            val = prod + (prod*0.20)
            print('Você irá pagar R${:.3f}'.format(val))
elif car=='NÃO':
    print('O pagamento então será no dinheiro ou cheque!')
    din = prod - (prod*0.10)
    print('O valor do produto será R${:.3f}'.format(din))
