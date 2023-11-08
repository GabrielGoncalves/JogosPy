import adivinhacao
import forca


def painel():
    print("Bom vindo a seleção de jogos!")
    print("Selecione o seu jogo, [1]Adivinhação   [2]Forca ")

    jogo = int(input("Digite o seu codigo: "))

    if (jogo == 1):
        print("Iniciando Adivinhação!")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Iniciando Forca!")
        forca.jogar()
    else:
        print("Código incorreto, por favor selecione um código válido.")
