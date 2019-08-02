import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = []

    #opcao de segurança para usar o open
    #o with fecha o arquivo automaticamente, mesmo se ocorrer um erro
    with open("C:/Users/pedro/Documents/ALURA/Python/jogo/words.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())


    posicao = random.randrange(0,len(palavras))

    palavra = palavras[posicao]

    # List Comprehension
    letras_acertadas = ["_" for letra in palavra]
    index = 0

    enforcado = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcado and not acertou):
        desenha_forca(erros)
        letra_jogador = input("Digite uma letra->")

        #remove espaços em branco na string
        letra_jogador = letra_jogador.strip().lower();

        if(letra_jogador in palavra and not (letra_jogador in letras_acertadas) ):
            index = 0
            for letra in palavra:
                if(letra.lower() == letra_jogador):
                    letras_acertadas[index] = letra.lower()
                index += 1
            print(letras_acertadas)

        else:
            #entra no erro quando não existe a letra na palavra secreta e quando o jogador já escolheu essa letra anteriormente
            erros += 1
            tentativas = 7 - erros
            print("Você tem " + str(tentativas) + " tentativas...")

        enforcado = erros == 7
        acertou = '_' not in letras_acertadas

    desenha_forca(erros)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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



def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()