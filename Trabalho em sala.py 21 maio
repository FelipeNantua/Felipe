import random

def adivinhe_o_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativa = 0
    acertou = False
    print("adivinhe o numero 1 e 100")
    
    while not acertou:
        palpite = int(input("digite seu palpite: "))
        tentativa += 1
        if palpite < numero_aleatorio:
            print("muito baixo")
        elif palpite > numero_aleatorio:
            print("muito alto!")
        else:
            print("voce adivinhou em (tentativa) tentativas")
            acertou = True

import random

def lancamento_dado():
    # Simula o lançamento do dado
    resultado = random.randint(1, 6)
    return resultado

# Teste da função
resultado_lancamento = lancamento_dado()
print("O resultado do lançamento do dado é:", resultado_lancamento)
