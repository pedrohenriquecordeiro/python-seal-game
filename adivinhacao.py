import random

def jogar():
    numero_pontos = 1000
    pontos_perdidos = 0

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("Existe um numero sorteado ... Se você descobrir qual é o numero você ganha")
    nome = input("Mas antes ... Qual seu nome?")

    #input do python3 sempre retorna uma string para a variavel /// no python 2 ele tipa dinamicamente
    print("Olá " + nome + "!!! Iremos começar. De inicio você terá " + str(numero_pontos) + " pontos ta!? ...Boa sorte ok !?")
    print( "Mas olha só, apenas escolha numeros dentro do intervalo de 0 a 100 ta bom ? \n")
    print("Vamos apenas escolher o nível de dificuldade!")
    print("(1) Fácil (2) Médio (3) Difícil")

    while( 1 ):
        dificuldade = int(input("Qual você quer " + nome + "?" ))
        if( int(dificuldade) == 1 or int(dificuldade) == 2 or int(dificuldade) == 3):
            print("\n")
            break
        else:
            print("Apenas 1 , 2 ou 3 são aceitos " + nome)

    numero_secreto = round(random.randrange(1,101))

    if( int(dificuldade) == 1):
        numero_tentativas = 10
    elif( int(dificuldade) == 2):
        numero_tentativas = 7
    elif( int(dificuldade) == 3):
        numero_tentativas = 5

    for numero_rodada in range(1,numero_tentativas+1):
        print( "Tentativa:" + str(numero_rodada) + " de " + str(numero_tentativas) )
        chute = input( nome + " digite o numero que o você acha que nós escolhemos ...")

        if( int(chute) < 0 or int(chute)>100):
            print("puts cara , apenas numero entre 0 e 100 , lembre-se disso\n")
            continue

        acertou = ( int(chute) == numero_secreto )
        if acertou :
            print("Você acertou ! Parabens")
            print("Seus pontos " + str(numero_pontos))
            break
        else :
            if( numero_secreto > int(chute) ):
                print("Quase, o numero secreto é MAIOR ..\n")
                pontos_perdidos = numero_secreto - int(chute)
                numero_pontos -= pontos_perdidos
            elif( numero_secreto < int(chute) ):
             print("Quase, o numero secreto era MENOR ..\n")
             pontos_perdidos = int(chute) -  numero_secreto
             numero_pontos -= pontos_perdidos


if(__name__ == "__main__"):
    jogar()