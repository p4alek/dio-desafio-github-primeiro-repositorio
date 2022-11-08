# Hangman Game
# Programação Orientada a Objetos

from random import randint

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    letras_erradas = ''
    letras_corretas = ''
    count_erradas = 0
    count_corretas = 0

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            Hangman.letras_corretas += letter + '\n'
            Hangman.count_corretas += 1
        else:
            Hangman.letras_erradas += letter + '\n'
            Hangman.count_erradas += 1

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return Hangman.count_erradas == 6

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return Hangman.count_corretas == len(set(self.word))

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for i in self.word:
            if i not in Hangman.letras_corretas:
                rtn += '_'
            else:
                rtn += i
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[Hangman.count_erradas])
        print(f'Palavra: {self.hide_word()}\n')
        print(f'Letras erradas: {Hangman.letras_erradas}\n')
        print(f'Letras corretas: {Hangman.letras_corretas}\n')

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras_forca.txt.txt", "rt") as f:
        bank = f.readlines()
    return bank[randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    while not game.hangman_over():
        if game.hangman_won():
            break
        else:
            game.print_game_status()
            letter = input('Digite uma palavra: ')
            game.guess(letter)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()