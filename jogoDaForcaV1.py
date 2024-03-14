# Projeto 1
# Desenvolvimento do Jogo da Forca
# Projeto desenvolvido em conjunto com as aulas da DSA

# imports:
import random
from os import system, name

# função para limpar a tela:
def limpaTela():
    
    # se windows...
    if name == 'nt':
        _ = system('cls')
    # senão (é mac ou linux)
    else:
        _ = system('clear')

def jogo():

    limpaTela()

    print("\nEste é o jogo da forca!")
    print("Advinhe qual é a palavra abaixo:\n")

    # lista de palavras
    # esta foi montada manualmente:
    listaPalavras = ['abacaxi', 'manga', 'banana', 'uva', 'abacate', 'morango']

    # uso do random para escolher uma palavra aleatória:
    palavraAleatoria = random.choice(listaPalavras)

    # list comprehension para printar os _'s:
    letrasPropostas = ['_' for letra in palavraAleatoria]

    # chances:
    chances = 6

    # listagem de letras erradas:
    letrasErradas = []