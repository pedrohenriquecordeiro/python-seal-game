import forca
import adivinhacao

def escolher_jogo() :
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    while(1):
        jogo = int(input("Qual jogo? "))

        if (jogo == 1):
            print("Abrindo o jogo da forca")
            break
        elif (jogo == 2):
            print("Abrindo o jogo da adivinhação")
            break
        else:
            print("Apenas 1 ou 2")

    if( jogo == 1):
        forca.jogar()
    elif( jogo == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    #se eu sou o principal eu run
    #se eu for chamado por um outro arquivo eu não sou principal entao eu nao dou run
    escolher_jogo()