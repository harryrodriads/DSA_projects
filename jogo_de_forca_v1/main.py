import random
from os import system, name

def game():
    print("Bem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    print("Dica: OBJETO\n")

    palavras = ['bola', 'chave', 'caneta', 'caderno', 'mochila']
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê GANHOU!!! A palavra era:", palavra, "!")
            break

    if "_" in letras_descobertas:
        print("\nVocê PERDEU... A palavra era:", palavra, "!")


if __name__ == "__main__":
    game()
    print("\nEsse é um jogo que aprendi na DSA. :)\n")