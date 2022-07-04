import forca
import adivinha


def escolhe_jogo():
    print("********************************")
    print("********escolha o joga**********")
    print("********************************")

    jogo = int(input("\n(1) Forca (2) Adivinhação\n\n "
                     "Qual jogo?: "))

    if jogo == 1:
        print("\nJogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")

        adivinha.jogar()


if __name__ == "__main__":
    escolhe_jogo()
