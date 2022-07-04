import random


def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 100

    nivel = int(input("\nQual nivel de dificuldade?\n\n"
                      "(1) Facil (2) Medio (3) Dificil\n\n"
                      "Defina o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um numero de 1 a 100: "))
        print("\nVoce digitou", chute)

        if chute < 1 or chute > 100:
            print("\nApenas numeros de 1 a 100")
            continue

        if numero_secreto == chute:
            print(f"\nVoce acertou e fez {pontos} pontos")
            break

        else:
            if chute > numero_secreto:
                print("\nVoce errou! O seu chute foi maior do que o numero secreto.")

            elif chute < numero_secreto:
                print("\nVoce errou! O seu chute foi menor do que o numero secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f"\nFim do jogo, o numero era {numero_secreto}")


if __name__ == "__main__":
    jogar()
