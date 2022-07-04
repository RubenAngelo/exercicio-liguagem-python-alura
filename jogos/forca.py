import random


def jogar():
    imprime_mensagem_abertura()

    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    escolha = random.randrange(0, len(palavras))
    palavra_secreta = palavras[escolha].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        print(f"\nVoce pode errar mais {abs(erros - len(palavra_secreta))} vezes")

        print(f"\n{letras_acertadas}\n")

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            print(f"\nNão tem {chute} na frase secreta")
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas

        if index == len(palavra_secreta):
            print(f"\nVoce acertou, tem {palavra_secreta.count(chute)}ª letras {chute} na palavra secreta")

    if acertou:
        print(f"{letras_acertadas}\n")
        print("Voce ganhou!!")
    else:
        print("Voce perdeu")

    print(f"\nFim do jogo")


def imprime_mensagem_abertura():
    print("\n********************************\n"
          "***Bem vindo ao jogo da forca***\n"
          "********************************\n")


if __name__ == "__main__":
    jogar()
