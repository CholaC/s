import pygame #import module for canvas
from random import randint #randomness for tile generation

#
def moveLeft():
    # move the tiles left
    tilesToMove = []
    canContinue = True;
    for y in range(gameBoardHeight):
        for x in range(gameBoardWidth):
            if gameBoard[y][x] == 8:
                tilesToMove.append((y, x))

                if (x == 0):
                    if (gameBoard[y][gameBoardWidth - 1] != 0 and gameBoard[y][gameBoardWidth - 1] != 8):
                        return;
                else:
                    if (gameBoard[y][x - 1] != 0 and gameBoard[y][x - 1] != 8):
                        return;

    for n in range(len(tilesToMove)):
        gameBoard[tilesToMove[n][0]][tilesToMove[n][1]] = 0
    for n in range(len(tilesToMove)):
        if tilesToMove[n][1] == 0:
            tilesToMove[n] = [tilesToMove[n][0], gameBoardWidth]
        gameBoard[tilesToMove[n][0]][tilesToMove[n][1] - 1] = 8


def moveRight():
    # move the tiles right
    tilesToMove = []
    for y in range(gameBoardHeight):
        for x in range(gameBoardWidth):
            if gameBoard[y][x] == 8:
                tilesToMove.append((y, x))

                if (x == gameBoardWidth - 1):
                    if (gameBoard[y][0] != 0 and gameBoard[y][0] != 8):
                        return;
                else:
                    if (gameBoard[y][x + 1] != 0 and gameBoard[y][x + 1] != 8):
                        return;
                        # Case x < width-1

    for n in range(len(tilesToMove)):
        gameBoard[tilesToMove[n][0]][tilesToMove[n][1]] = 0
    for n in range(len(tilesToMove)):
        if tilesToMove[n][1] == gameBoardWidth - 1:
            tilesToMove[n] = [tilesToMove[n][0], -1]
        gameBoard[tilesToMove[n][0]][tilesToMove[n][1] + 1] = 8


def tileFall():
    # moves the moving tiles down
    for y in range(gameBoardHeight - 1, -1, -1):
        for x in range(gameBoardWidth - 1, 0, -1):
            if gameBoard[y][x] == 1 or gameBoard[y][x] == 2 or gameBoard[y][x] == 3 or gameBoard[y][x] == 4 or \
                            gameBoard[y][x] == 5 or gameBoard[y][x] == 6 or gameBoard[y][x] == 7:
                if gameBoard[y + 1][x] == 0:
                    temp = gameBoard[y][x]
                    gameBoard[y][x] = 0
                    gameBoard[y + 1][x] = temp


def getNextBlock():
    # randomly generate the next block used
    newBlock = randint(1, 7)
    newBlock = 2
    arr = []

    #7 block shape types
    if newBlock == 1:
        # line block
        arr.insert(0, [-2, 0])
        arr.insert(0, [-1, 0])
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
    elif newBlock == 2:
        # L block
        arr.insert(0, [-1, 0])
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
        arr.insert(0, [1, 1])
    elif newBlock == 3:
        # Backward L block:
        arr.insert(0, [-1, 0])
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
        arr.insert(0, [1, -1])
    elif newBlock == 4:
        # T Block
        arr.insert(0, [-1, 0])
        arr.insert(0, [0, 0])
        arr.insert(0, [0, 1])
        arr.insert(0, [1, 0])
    elif newBlock == 5:
        # square block
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
        arr.insert(0, [0, 1])
        arr.insert(0, [1, 1])
    elif newBlock == 6:
        # Z block
        arr.insert(0, [0, 1])
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
        arr.insert(0, [1, -1])
    elif newBlock == 7:
        # S block
        arr.insert(0, [1, 1])
        arr.insert(0, [0, 0])
        arr.insert(0, [1, 0])
        arr.insert(0, [0, -1])

    rotation = randint(0, 3)
    rotateArr(rotation, arr, newBlock)


# slow down locking
# movement speed up

# add the rotated array to the thing here
# input arrs must be able to fit within a 5x5

def rotateArr(rotation, arr, type):
    matrix = []
    if rotation == 1:  # 90 degrees cw
        matrix.insert(0, [0, 1])
        matrix.insert(1, [-1, 0])
    if rotation == 2:  # 180 degrees cw
        matrix.insert(0, [-1, 0])
        matrix.insert(1, [0, -1])
    if rotation == 3:  # 270 degrees cw
        matrix.insert(0, [0, -1])
        matrix.insert(1, [1, 0])

    if rotation > 0:
        returnArr = []
        for coord in arr:
            x = coord[0]  # Center them at 0, add 2 to both at end
            y = coord[1]
            newX = x * matrix[0][0] + y * matrix[1][0]
            newY = x * matrix[0][1] + y * matrix[1][1]

            returnArr.insert(0, [newX, newY])
    else:
        returnArr = arr

    for coord in returnArr:
        gameBoard[coord[1] + 2][coord[0] + 4] = type


def draw():
    gameScreen.fill((255, 255, 255))

    # Replace This section with an actual good UI
    pygame.draw.rect(gameScreen, (50, 50, 150), (0, 0, gameBoardWidth / 2 * tileSize * scale, 20 * tileSize), 0)
    pygame.draw.rect(gameScreen, (50, 50, 150), (
        gameBoardWidth * tileSize * scale * 3 / 2, 0, gameBoardWidth / 2 * tileSize * scale, 20 * tileSize), 0)
    # SCORE COUNTER AT TOP

    for y in range(len(gameBoard)):
        for x in range(len(gameBoard[y])):
            if gameBoard[y][x] >= 1:
                if gameBoard[y][x] == 1:
                    gameScreen.blit(BLUE_blockImage, (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 2:
                    gameScreen.blit(CYAN_blockImage, (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 3:
                    gameScreen.blit(GREEN_blockImage,
                                    (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 4:
                    gameScreen.blit(ORANGE_blockImage,
                                    (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 5:
                    gameScreen.blit(PURPLE_blockImage,
                                    (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 6:
                    gameScreen.blit(RED_blockImage, (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 7:
                    gameScreen.blit(YELLOW_blockImage,
                                    (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))
                if gameBoard[y][x] == 8:
                    gameScreen.blit(GREY_blockImage, (x * tileSize + gameBoardWidth / 2 * tileSize, (y - 4) * tileSize))

                    # print(gameBoard[y][x], end="")
                    # print()
                    # print()
    pygame.display.update()

#checks when falling block reaches the bottom stack
def isBlockStoped():
    for y in range(gameBoardHeight - 1, 0, -1):
        for x in range(gameBoardWidth - 1, 0, -1):
            if gameBoard[y][x] == 1 or gameBoard[y][x] == 2 or gameBoard[y][x] == 3 or gameBoard[y][x] == 4 or \
                            gameBoard[y][x] == 5 or gameBoard[y][x] == 6 or gameBoard[y][x] == 7:
                if y == (gameBoardHeight - 1):
                    return True
                if gameBoard[y + 1][x] == 8:
                    return True


def stopBlock():
    global counter
    breakOut = False
    if counter > 1:
        for y in range(gameBoardHeight - 1, 0, -1):
            for x in range(gameBoardWidth - 1, 0, -1):
                if gameBoard[y][x] == 1 or gameBoard[y][x] == 2 or gameBoard[y][x] == 3 or gameBoard[y][x] == 4 or \
                                gameBoard[y][x] == 5 or gameBoard[y][x] == 6 or gameBoard[y][x] == 7:
                    gameBoard[y][x] = 8
                    clearComplete()
                    breakOut = True
                    break
            if (breakOut):
                break

        counter = 0
    else:
        counter += 1

## You lose when the falling block reaches the top of the
def loseGame():
    for y in range(3, 0, -1):
        for x in range(gameBoardWidth - 1):
            if gameBoard[y][x] == 8:
                return True

#handle when user press arrow keys
def processInput():
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                moveLeft()
            if event.key == pygame.K_RIGHT:
                moveRight()


def checkNextBlock():
    for y in range(gameBoardHeight - 1, 0, -1):
        for x in range(gameBoardWidth - 1, 0, -1):
            if gameBoard[y][x] < 8 and gameBoard[y][x] > 0:
                return;
    getNextBlock()


def clearComplete():
    global delay_interval
    scoreMod = 0
    for y in range(gameBoardHeight - 1, 0, -1):
        lineCount = 0;
        for x in range(gameBoardWidth - 1, -1, -1):
            if (gameBoard[y][x] == 8):
                lineCount += 1
        if (lineCount == gameBoardWidth):
            del gameBoard[y]
            gameBoard.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0])
            scoreMod += 1

    delay_interval -= scoreMod * 5
    if (delay_interval < 25):
        delay_interval = 25
    # print (scoreMod)
    return scoreMod

#load song from resources
def getSong(song):
    pygame.mixer.music.load(song)



delay_interval = 150
counter = 0


def init():
    #initialize global vars
    #tetris board
    global gameBoardHeight
    global gameBoardWidth
    global gameBoard
    global gameScreen

    #physics vars
    global delay_interval
    global time
    global scale

    #falling blocks
    global tileSize # pixel size of images
    global BLUE_blockImage
    global CYAN_blockImage
    global GREEN_blockImage
    global ORANGE_blockImage
    global RED_blockImage
    global PURPLE_blockImage
    global YELLOW_blockImage
    global GREY_blockImage

    #import coloured block from resources folder
    BLUE_blockImage = pygame.image.load("resources/BLUE_BOX.png")
    CYAN_blockImage = pygame.image.load("resources/CYAN_BOX.png")
    GREEN_blockImage = pygame.image.load("resources/GREEN_BOX.png")
    ORANGE_blockImage = pygame.image.load("resources/ORANGE_BOX.png")
    RED_blockImage = pygame.image.load("resources/RED_BOX.png")
    PURPLE_blockImage = pygame.image.load("resources/PURPLE_BOX.png")
    YELLOW_blockImage = pygame.image.load("resources/YELLOW_BOX.png")
    GREY_blockImage = pygame.image.load("resources/STOPED_SQUARE.png")

    #music background sound
    introSong = "resources/A_Intro.ogg"
    mainSong = "resources/A_Main.ogg"

    #inilialize physics vars
    scale = 1
    time = 0

    #init the tiles
    tileSize = 32
    tileContains = 0

    # init the game board size
    gameBoardHeight = 22
    gameBoardWidth = 9
    gameBoard = [[tileContains for x in range(gameBoardWidth)] for y in range(gameBoardHeight)]

    #set up pygame canvas
    pygame.init()
    gameScreen = pygame.display.set_mode(
        (tileSize * gameBoardWidth * scale * 2, tileSize * (gameBoardHeight - 4) * scale + scale))

    # init the tiles and game board size -- possibly redundant
    time = 0
    tileContains = 0
    gameBoardHeight = 22
    gameBoardWidth = 9

    #animation vars
    delay_interval = 125
    counter = 0

    # init the game board
    gameBoard = [[tileContains for x in range(gameBoardWidth)] for y in range(gameBoardHeight)]
    draw()
    getNextBlock()
    draw()
    pygame.mixer.music.set_volume(5)
    getSong(introSong)
    pygame.mixer.music.play(1)


    #core loop - draw
    while (not loseGame()):
        if pygame.mixer.music.get_busy() == False:
            getSong(mainSong)
            pygame.mixer.music.play(-1)

        processInput()
        counter += 1
        if isBlockStoped():
            stopBlock()
        else:
            if counter >= 2:
                tileFall()
                counter = 0
        draw()
        checkNextBlock()
        pygame.time.wait(delay_interval)

    draw()


init()
