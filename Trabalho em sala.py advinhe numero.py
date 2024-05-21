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