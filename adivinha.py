import random #Essa é uma função buildin que não vem pronta, se quiser usar devemos importar, e quando não é utilizada fica em cinza
def adivinha():
    print("************************************************************************")
    print("Jogo de adivinhação")
    print("Escolhi um numero de 1 a 100, tente acertar o meu número secreto")
    print("BOA SORTE")
    print("************************************************************************")

    numero_secreto = random.randrange(1, 101) #Numero secreto vai de 1 a 100 pois não inclui. (apenas o lado x inclui (x,y))
    pontos = 1000 #Pontos totais, vão sendo subtraidos de acordo com palpite

    tentativas = 4

    print("Qual o nivel de dificuldade que você prefere?")
    print("Opções: 1 = facil, 2 = médio e 3 = dificil ou 4 = aleatorio")

    nivel = int(input("Defina o nivel: ")) #Entrada do usuario

    if (nivel == 1):
        tentativas = 10
        print("Você está jogando no facil, atualmente possui ", tentativas, "tentativas.")
        pontos = pontos - 400
    elif (nivel == 2):
        tentativas = 7
        print("Você está no jogando no médio, atualmente possui ", tentativas, "tentativas.")
        pontos = pontos - 200
    elif (nivel == 3):
        tentativas = 5
        pontos = pontos + 100
        print("Você está no jogando no dificil, atualmente possui ", tentativas, "tentativas.")
    elif (nivel == 4):
        tentativas = random.choice([15, 7, 3])
        print("Você está no jogando no modo aleatorio, atualmente possui ", tentativas, "tentativas.")

    while (nivel < 1 or nivel > 4):
        print("Você deve escolher um nivel de 1 a 4")
        nivel = int(input("Defina o nivel: "))
        continue





    while (tentativas > 0):
        chute = input("Digite aqui o seu chute: ")
        chutenumero = int(chute)
        print("")
        print("Resta(m)", tentativas - 1, "tentativas.")
        print("")
        pontos_perdidos = abs(numero_secreto - chutenumero)

        if (chutenumero < 1 or chutenumero > 100):
            print("Você deve digitar um número de 1 a 100")
            continue

        acertou = numero_secreto == chutenumero
        errou_para_mais = numero_secreto > chutenumero
        errou_para_menos = numero_secreto < chutenumero


        if (tentativas <= 0):
            print("Acabaram seus chutes, você PERDEU!")
            pontos = pontos - 500

        else:
            if (errou_para_mais):
                print("Você chutou baixo.")
                print("")
                print("Tente novamente")
                print("")
                tentativas = tentativas - 1
                pontos = pontos - pontos_perdidos


                if (tentativas == 0):
                    print("Acabaram seus chutes, você PERDEU!")
                    print("")
                    print("O número secreto era ", numero_secreto, ".")
                    pontos = pontos - 500

            elif (errou_para_menos):
                print("Você chutou alto.")
                print("")
                print("Tente novamente")
                print("")
                tentativas = tentativas - 1
                pontos = pontos - pontos_perdidos
                if (tentativas == 0):
                    print("Acabaram seus chutes, você PERDEU!")
                    pontos = pontos - 500
                    print("O número secreto era ", numero_secreto)


            elif (acertou):
                print("você acertou em cheio, VIVA O VENCEDOR(A)")
                print("O número secreto era ", numero_secreto)
                tentativas = tentativas - 4
                break

    print("")
    print("Sua pontuação =", pontos)
    print("")
    print("FIM DO JOGO")


if(__name__== "__main__"):
    adivinha()

