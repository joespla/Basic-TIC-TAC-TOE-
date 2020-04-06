from random import randrange


def DisplayBoard(board):
    #
    # La función acepta un parametro el cual contiene el estado actual del tablero y lo muestra en la consola
    #
    for i in range(len(board)):
        for j in board[i]:
            print (j, end = " ")
        print("\n")


def EnterMove(board):
    #
    # La función acepta el estaduo actual del trablero y pregunta al usuario de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    return None


def MakeListOfFreeFields(board):
    #
    # La función examina el tablero y construye una lista de todos los cuadros vacios
    # La lista está compuesta por tuplas, cada tupla es un par de número que indican la fila y columna
    #
    return None


def VictoryFor(board, sign):
    #
    # La función analiza el estatus del tablero para verificar si el jugador que utiliza las 'o' o las 'x' ha ganado el juego
    #
    #
    return None


def DrawMove(board):
    #
    # La función dibuja el movimiento de la maquina y actualiza el tablero
    #
    for i in range(10):
        print(randrange(8))


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

