from random import randrange
import time


def DisplayBoard(board):
    #
    # La función acepta un parametro el cual contiene el estado actual del tablero y lo muestra en la consola
    #
    for i in range(len(board)):
        for j in board[i]:
            print(j, end=" ")
        print("\n")


def EnterMove(board):
    #
    # La función acepta el estaduo actual del trablero y pregunta al usuario de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    boardUpdate = board[:]
    del (mainBoard[:])
    verification = True
    aux = []
    count = 1
    userMovement = int(input("Make a move. Tell me where you want to play: "))

    # Verifica los movimiento ya jugados
    for i in range(3):
        for j in range(3):
            if boardUpdate[i][j] == "X" or boardUpdate[i][j] == "O":
                count += 1
            else:
                aux.append(count)
                count += 1

    # Checa que el movimiento no exista
    while verification:
        if userMovement in aux:
            verification = False
        else:
            DisplayBoard(boardUpdate)
            userMovement = int(input("Make a valid move... Tell me where you want to play: "))

    # Busca la posicion dada por el usuario y la ingresa en el tablero
    for line in range(3):
        for column in range(3):
            if boardUpdate[line][column] == userMovement:
                boardUpdate[line][column] = 'O'
                break

    DisplayBoard(boardUpdate)
    return boardUpdate


def MakeListOfFreeFields(board):
    #
    # La función examina el tablero y construye una lista de todos los cuadros vacios
    # La lista está compuesta por tuplas, cada tupla es un par de número que indican la fila y columna
    #
    return None


def VictoryFor(board):
    #
    # La función analiza el estatus del tablero para verificar si el jugador que utiliza las 'o' o las 'x' ha ganado el juego
    #
    #
    boardUpdate = board[:]

    if (boardUpdate[0][0] == "X" and boardUpdate[0][1] == "X" and boardUpdate[0][2] == "X") or (boardUpdate[0][0] == "O" and boardUpdate[0][1] == "O" and boardUpdate[0][2] == "O"):
        return False
    elif (boardUpdate[1][0] == "X" and boardUpdate[1][1] == "X" and boardUpdate[1][2] == "X") or (boardUpdate[1][0] == "O" and boardUpdate[1][1] == "O" and boardUpdate[1][2] == "O"):
        return False
    elif (boardUpdate[2][0] == "X" and boardUpdate[2][1] == "X" and boardUpdate[2][2] == "X") or (boardUpdate[2][0] == "O" and boardUpdate[2][1] == "O" and boardUpdate[2][2] == "O"):
        return False
    elif (boardUpdate[0][0] == "X" and boardUpdate[1][0] == "X" and boardUpdate[2][0] == "X") or (boardUpdate[0][0] == "O" and boardUpdate[1][0] == "O" and boardUpdate[2][0] == "O"):
        return False
    elif (boardUpdate[0][1] == "X" and boardUpdate[1][1] == "X" and boardUpdate[2][1] == "X") or (boardUpdate[0][1] == "O" and boardUpdate[1][1] == "O" and boardUpdate[2][1] == "O"):
        return False
    elif (boardUpdate[0][2] == "X" and boardUpdate[1][2] == "X" and boardUpdate[2][2] == "X") or (boardUpdate[0][2] == "O" and boardUpdate[1][2] == "O" and boardUpdate[2][2] == "O"):
        return False
    elif (boardUpdate[0][0] == "X" and boardUpdate[1][1] == "X" and boardUpdate[2][2] == "X") or (boardUpdate[0][0] == "O" and boardUpdate[1][1] == "O" and boardUpdate[2][2] == "O"):
        return False
    elif (boardUpdate[0][2] == "X" and boardUpdate[1][1] == "X" and boardUpdate[2][0] == "X") or (boardUpdate[0][2] == "O" and boardUpdate[1][1] == "O" and boardUpdate[2][0] == "O"):
        return False
    else:
        return True


def DrawMove(board):
    #
    # La función dibuja el movimiento de la maquina y actualiza el tablero
    #
    boardUpdate = board[:]
    del (mainBoard[:])
    machineMovement = randrange(1, 10)
    aux = []
    count = 1
    verification = True

    for i in range(3):
        for j in range(3):
            if boardUpdate[i][j] == "X" or boardUpdate[i][j] == "O":
                count += 1
            else:
                aux.append(count)
                count += 1

    while verification:
        if machineMovement in aux:
            verification = False
        else:
            machineMovement = randrange(1, 9)

    for line in range(3):
        for column in range(3):
            if boardUpdate[line][column] == machineMovement:
                boardUpdate[line][column] = 'X'
                break

    print("The computer is moving... The computer chose position: ", machineMovement)
    DisplayBoard(boardUpdate)
    return boardUpdate


mainBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
auxBoard = []
startGame = True


while startGame:
    auxBoard = DrawMove(mainBoard)
    mainBoard = auxBoard[:]
    del (auxBoard[:])
    startGame = VictoryFor(mainBoard)
    if startGame:
        auxBoard = EnterMove(mainBoard)
        mainBoard = auxBoard[:]
        del (auxBoard[:])
        startGame = VictoryFor(mainBoard)

print("***************************")
DisplayBoard(mainBoard)
print("El juego ha terminado")
