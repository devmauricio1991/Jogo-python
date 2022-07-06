import forca
import adivinha

def teste():
    print("******************")
    print("Escolha o seu jogo")
    print("******************")
    print("")
    print("Digite:")
    print("(1) Jogo Forca")
    print("(2) Jogo Adivinha")
    print("")
    print("Qual jogo gostaria de jogar?")



    escolha_jogo = int(input("Digite: "))


    if(escolha_jogo == 1):

        print("Você escolheu jogar Forca. Seja bem vindo")
        forca.forca()
        print("O que gostaria de fazer?")
        print("(1) - Jogar novamente")
        print("(2) - Voltar ao MENU")
        escolha_final_um = int(input("Digite: "))
        if (escolha_final_um == 1):
            forca.forca()

        elif (escolha_final_um == 2):
            teste()

    elif(escolha_jogo == 2):
        print("Você escolheu jogar Adivinhação. Seja bem vindo")
        adivinha.adivinha()
        print("O que gostaria de fazer?")
        print("(1) - Jogar novamente")
        print("(2) - Voltar ao MENU")
        escolha_final_dois = int(input("Digite: "))
        if (escolha_final_dois == 1):
            adivinha.adivinha()
        elif (escolha_final_dois == 2):
            teste()


teste()