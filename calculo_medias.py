print('Olá, sou um programa desenvolvido para você verificar suas notas ;-;\n')

T1 = float(input('Digite sua primeira nota: '))
T2 = float(input('Digite a segunda nota: '))
T3 = float(input('Digite a terceira nota: '))
s = T1 + T2 + T3
Ma = s / 3

print('\nA soma das notas trimestrais foi de: {:.1f}'.format(s))
print('E a média trimestral foi de: {:.1f}\n'.format(Ma))

if Ma >= 7.0:
    print('Parabéns, você passou por nota! ;-;')
    exit()
else:
    f = float(input('Qual foi a nota da média final? '))
    Sf = round((f + Ma)/2, 1)

    if Sf >= 5.0:
        print('Parabéns, você passou na final!')
    else:
        print('Infelizmente, você não recuperou na final!')