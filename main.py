import random
import json
from datetime import datetime




locations = []
scoreBack = []

EMPTY = 'E'
TREASURE = 'T'
MONSTER = 'M'
SWORD = 'S'
POTION = 'P'
VENOM = 'V'

whatToAddInGrid = (TREASURE, TREASURE, TREASURE, TREASURE, TREASURE, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, SWORD,
                   SWORD, POTION, POTION, POTION, VENOM, VENOM, VENOM)

NROWS_IN_GRID = 6
NCOLS_IN_GRID = 8

grid = []
gridEmpty = []

for r in range(0, NROWS_IN_GRID):  # 0-5
    aRow = []
    for c in range(0, NCOLS_IN_GRID):  # 0-7
        aRow.append(EMPTY)
    grid.append(aRow)

for r in range(0, NROWS_IN_GRID):  # 0-5
    aRow = []
    for c in range(0, NCOLS_IN_GRID):  # 0-7
        aRow.append(' ')
    gridEmpty.append(aRow)

def findEmptyCell(aGrid, nRows, nCols):
    # Find a random starting cell that is empty.
    while True:
        row = random.randrange(nRows)
        col = random.randrange(nCols)
        if aGrid[row][col] == EMPTY:
            return row, col


for item in whatToAddInGrid:
    rowRandom, colRandom = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
    grid[rowRandom][colRandom] = item

# Setting the starting cell
startRow, startCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
#print('Starting at row:', startRow + 1, 'col:', startCol + 1)

for row in gridEmpty:
    gridEmpty[startRow][startCol] = grid[startRow][startCol]
    print(row)

def eGPrint():
    for row in gridEmpty:
        print(row)


score = 0
swordN = 0
potionN = 0
while True:
    # move the user around
    direction = input('Press L, U, R, D to move: ').lower()
    print()


    if direction == 'l':
        locations.append("l")
        if startCol == 0:
            startCol = NCOLS_IN_GRID - 1
        else:
            startCol -= 1
    elif direction == 'r':
        locations.append("r")
        if startCol == NCOLS_IN_GRID - 1:
            startCol = 0
        else:
            startCol += 1
    elif direction == 'u':
        locations.append("u")
        if startRow == 0:
            startRow = NROWS_IN_GRID - 1
        else:
            startRow -= 1
    elif direction == 'd':
        locations.append("d")
        if startRow == NROWS_IN_GRID - 1:
            startRow = 0
        else:
            startRow += 1
    else:
        print('Invalid move. Quitting the game.')
        break

    foundInCell = grid[startRow][startCol]
    #print('Now at row', startRow + 1, ' col:', startCol + 1, ' cell contains:', foundInCell)
    print("Score:", score, " Sword and Potion:", swordN, ";", potionN)

    if foundInCell == "T":
        score += 2
        scoreBack.append(score)
        print("----------------------\n\n"
              "+TREASURE\n\n"
              "----------------------")
        grid[startRow][startCol] = "X"
        gridEmpty[startRow][startCol] = "T"
        eGPrint()
        print("Score:", score, " Sword and Potion:", swordN, ";", potionN)
    elif foundInCell == "E":
        score += 1
        scoreBack.append(score)
        print("----------------------\n\n"
              "+SCORE\n\n"
              "----------------------")
        grid[startRow][startCol] = "X"
        gridEmpty[startRow][startCol] = "E"
        eGPrint()
        print("Score:", score, " Sword and Potion:", swordN, ";", potionN)
    elif foundInCell == "S":
        if swordN == 0:
            swordN += 1
            score += 1
            scoreBack.append(score)
            print("----------------------\n\n"
                  "+SWORD\n\n"
                  "----------------------")
            grid[startRow][startCol] = "X"
            gridEmpty[startRow][startCol] = "S"
            eGPrint()
            print("Score:", score, " Sword and Potion:", swordN, ";", potionN)
    elif foundInCell == "P":
        if potionN == 0:
            potionN += 1
            score += 1
            scoreBack.append(score)
            print("----------------------\n\n"
                  "+POTION\n\n"
                  "----------------------")
            grid[startRow][startCol] = "X"
            gridEmpty[startRow][startCol] = "P"
            eGPrint()
            print("Score:", score, " Sword and Potion:", swordN, ";", potionN)
    elif foundInCell == "M":
        if swordN == 0:
            print("----------------------\n\n"
                  "+Monster eat you. You are dead!!\n\n"
                  "----------------------")
            break
        elif swordN == 1:
            score += 1
            scoreBack.append(score)
            print("----------------------\n\n"
                  "+Oh, No! MONSTER.\n"
                  "SWORD is used.\n\n"
                  "----------------------")
            grid[startRow][startCol] = "X"
            gridEmpty[startRow][startCol] = "M"
            swordN -= 1
            eGPrint()
            print("Score:", score, " Sword and Potion:", swordN, ";", potionN)
    elif foundInCell == "V":
        if potionN == 0:
            print("----------------------\n\n"
                  "+Venom poisoned you. You are dead!!\n\n"
                  "----------------------")
            break
        elif potionN == 1:
            score += 1
            scoreBack.append(score)
            print("----------------------\n\n"
                  "+Oh, No! VENOM.\n"
                  "POTION is used.\n\n"
                  "----------------------")
            potionN -= 1
            grid[startRow][startCol] = "X"
            gridEmpty[startRow][startCol] = "V"
            eGPrint()
            print("Score:", score, " Sword and Potion:", swordN, ";", potionN)

    elif foundInCell == "X":
        print("----------------------\n\n"
              "+You already passed here.\n\n"
              "----------------------")
        eGPrint()
        if direction == 'l':
            if startCol == 0:
                startCol = NCOLS_IN_GRID + 1
            else:
                startCol += 1
        elif direction == 'r':
            if startCol == NCOLS_IN_GRID + 1:
                startCol = 0
            else:
                startCol -= 1
        elif direction == 'u':
            if startRow == 0:
                startRow = NROWS_IN_GRID + 1
            else:
                startRow += 1
        elif direction == 'd':
            if startRow == NROWS_IN_GRID + 1:
                startRow = 0
            else:
                startRow -= 1
dateTimePlayed = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

dictionary = {
    dateTimePlayed:{
        "score": scoreBack,
        "move": locations,
    }
}

json_object = json.dumps(dictionary, indent=3)

with open("sample.json", "a") as outfile:
   outfile.write(json_object)

