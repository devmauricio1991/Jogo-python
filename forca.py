def forca(): #isso é uma função, criamos para podermos chama-la em outro modulo.
    import random


    print("")
    print(" - - - - - - - - - - - - - - - - - Bem vindo ao JOGO DA FORCA - - - - - - - - - - - - - - - - - - - - -")
    print("")


    arquivo = open("palavras.txt", "r")
    palavras = []
    lista_letras_ja_escolhidas = []

    for linha in arquivo:
        linha = linha.strip() #Nesse caso o strip pode tirar elementos especiais, como espaços ou o \n (comando invisivel de pular a linha)
        palavras.append(linha) #append adiciona um item, nesse caso, adiciona a lista palavras []

    arquivo.close()


    contagem = open("palavras.txt", 'r')
    contagem_palavras_lista = 0
    for palavra in contagem:
        contagem_palavras_lista = contagem_palavras_lista + 1

    print("Temos o total de {} paravras secretas. Ao ganhar, você pode adicionar mais uma ao nosso banco de dados.".format(contagem_palavras_lista))

    contagem.close()

    lista_palavras_chave = palavras
    elemento = random.choice(lista_palavras_chave)
    palavra_chave = elemento
    quantia_letras_palavra_chave = len(palavra_chave) #len é para contar ou ver o tamanho da sequencia X (str é sequencia)
    letras_acertadas = ["_" for letra in palavra_chave] #Comprehensions - metodo de laço dentro da lista.


    # quadrados = [n*n for n in inteiros] - exemplo util de Comprehensions.

    print("")
    print("A palavra secreta possui {} letras. Tente adivinhar:".format(quantia_letras_palavra_chave))
    print(letras_acertadas)
    print("")

    enforcou = False
    acertou = False
    tentativas = 7

    print("Você tem {} vidas. Boa sorte.".format(tentativas)) #esse format serve para preencher o {} com oq quiser.
    print("")

    while(not enforcou and not acertou): #laço classico de while

        chute = input("Escolha uma letra: ")#entrada do usuario
        chute = chute.lower()#deixa tudo minusculo, inclusive a entrada do usuario
        chute = chute.strip()#remove os espaços
        lista_letras_ja_escolhidas.append(chute)
        print("Lista de letras já usadas: ", lista_letras_ja_escolhidas)


        if(chute in palavra_chave):
            posicao = 0
            for letra in palavra_chave: # Achei parecido com o método Comprehensions.
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1 # Poderiamos utilizar o += nesse caso para somar 1 a posição, por ciclo.


            acertou = "_" not in letras_acertadas # muda o acertou para False, terminando o laço.

            if (acertou == True):
                print("")
                print("A palavra secreta era {}.".format(elemento))
                print("")
                print("Você ganhou! PARABÉNS ! ! !")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\\:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \\::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")

                aumento_lista = input("Dê uma sugestão de palavra para usarmos no jogo. ESCREVA: ")
                pula_linha = ("\n")
                adicao = open("palavras.txt", "a")
                adicao.write(aumento_lista)
                adicao.write(pula_linha)
                adicao.close()



                print("")
                break # Outra maneira de terminar o laço

        else:
            tentativas = tentativas - 1
            print("Errou, não existe a letra {} na palavra.".format(chute))

            def desenha_forca(vidas):
                print("  _______     ")
                print(" |/      |    ")

                if (vidas == 6):
                    print(" |      (_)   ")
                    print(" |            ")
                    print(" |            ")
                    print(" |            ")

                if (vidas == 5):
                    print(" |      (_)   ")
                    print(" |      \     ")
                    print(" |            ")
                    print(" |            ")

                if (vidas == 4):
                    print(" |      (_)   ")
                    print(" |      \|    ")
                    print(" |            ")
                    print(" |            ")

                if (vidas == 3):
                    print(" |      (_)   ")
                    print(" |      \|/   ")
                    print(" |            ")
                    print(" |            ")

                if (vidas == 2):
                    print(" |      (_)   ")
                    print(" |      \|/   ")
                    print(" |       |    ")
                    print(" |            ")

                if (vidas == 1):
                    print(" |      (_)   ")
                    print(" |      \|/   ")
                    print(" |       |    ")
                    print(" |      /     ")

                if (vidas == 0):
                    print(" |      (_)   ")
                    print(" |      \|/   ")
                    print(" |       |    ")
                    print(" |      / \   ")

                print(" |            ")
                print("_|___         ")
                print()

            desenha_forca(tentativas)



        enforcou = tentativas == 0
        contagem = letras_acertadas.count("_")

        print(letras_acertadas)
        print("Você ainda tem {} vidas.".format(tentativas))
        print("Ainda temos letras {} faltando.".format(contagem))
        if (enforcou):
            print("")
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")
            print("")
            print("Suas chances acabaram. Você foi enforcado!!")
            print("")
            print("A palavra secreta era: {}.".format(elemento))
            print("")

#with open("palavras.txt") as arquivo:       <- essa técnica serve como modo de não ocorrer erro por não fechamento
    #for linha in arquivo:                      de arquivo, visto que é feito por baixo dos panos pelo pyton.
        #print(linha)                           Além disso parece ser um modo mais facil de abertura e execução de uma função.

if (__name__ == "__main__"):
    forca()