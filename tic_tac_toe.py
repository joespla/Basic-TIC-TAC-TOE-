from random import randrange
import time


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
    boardUpdate = board[:]
    del (mainBoard[:])
    #verification = True
    print("Make a move. Tell me where you want to move: ")
    userMovement = int(input())
    
    # Esto va a checar que el movimiento del usuario sea valida
    '''
    if userMovement not in boardUpdate:
        verification = False
        
        # Checa que el tiro del usuario sea valido
        while not verification:
            print ("Please make a valid move.")
            userMovement = int(input())
            if userMovement in boardUpdate:
                verification = True
    '''

    # Busca la posicion dada por el usuario y la ingresa en el tablero    
    for line in range(3):
        for column in range(3):
            if boardUpdate[line][column] == userMovement:
                boardUpdate[line][column] = 'O'
                break
            
    return boardUpdate


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
        print("Inicio del loop")
        time.sleep(1)
        if machineMovement in aux:
            verification = False
            print("Llego a aqui")
        else:
            machineMovement = randrange(1,9)

    for line in range(3):
        for column in range(3):
            if boardUpdate[line][column] == machineMovement:
                boardUpdate[line][column] = 'X'
                break
    
    print("The computer is moving...")
    print("The computer chose position: ", machineMovement)
    DisplayBoard(boardUpdate)
    return boardUpdate


mainBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
auxBoard = []
startGame = True

while startGame:
    auxBoard = DrawMove(mainBoard)
    mainBoard = auxBoard[:]
    del (auxBoard[:])
    auxBoard = EnterMove(mainBoard)
    mainBoard = auxBoard[:]
    del (auxBoard[:])
    DisplayBoard(mainBoard)
    


