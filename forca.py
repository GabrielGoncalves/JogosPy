import random
import jogos

def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(' '.join(letras_acertadas))

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = incremento()

        if(chute in palavra_secreta):
            marca_incremento_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            if(erros < 7):
                print(f'Ops, você errou! Faltam {7 - erros} tentativas.')
                desenha_forca(erros)
            else:
                print('Ops, você errou!')
                desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(' '.join(letras_acertadas))

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


def imprime_mensagem_de_abertura():

    print("***************************************************")
    print("************Bem vindo ao joga da forca!************")
    print("***************************************************")

def carregar_palavra_secreta():
    with open('palavras.txt') as arquivo:
        palavras = []

        for linhas in arquivo:
            linhas = linhas.strip()
            palavras.append(linhas)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def incremento():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute

def marca_incremento_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

def mensagem_vencedor():
    print('Parabéns! Você acertou.')
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

def mensagem_perdedor(palavra_secreta):
    print(f'Você errou! a palavra era {palavra_secreta.capitalize()}.')
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

if (__name__ == "__main__"):
    jogar()
