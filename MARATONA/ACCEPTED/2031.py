n = int(raw_input())

for i in range(n):
    a = raw_input()
    b = raw_input()

    if a == b:
        if a == 'ataque':
            print 'Aniquilacao mutua'
        elif a == 'papel':
            print 'Ambos venceram'
        else:
            print 'Sem ganhador'
    elif a == 'ataque':
        print 'Jogador 1 venceu'
    elif b == 'ataque' or b == 'pedra':
        print 'Jogador 2 venceu'
    elif a == 'pedra':
        print 'Jogador 1 venceu'