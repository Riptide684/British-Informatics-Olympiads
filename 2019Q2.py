#Sean Morrell - Aylesbury Grammar School

import sys


def check(location, board, facing):
    square = [0, 0]
    square[0] = location[0] + facing[0]
    square[1] = location[1] + facing[1]

    try:
        if board[square[1] - 1][square[0] - 1] != 0:
            return False

        else:
            return True

    except IndexError:
        return False


def update(board):
    for m in range(5):
        for n in range(5):
            if board[m][n] > 0:
                board[m][n] -= 1

    return board


grid = [[0]*5 for _ in range(5)]
position = [3, 3]
direction = [0, 1]

entry = input("Enter values: ")
values = entry.split(" ")
trail = int(values[0])
instructions = values[1]
turns = int(values[2])

for i in range(turns):
    instruction = instructions[i % len(instructions)]

    if instruction == "L":
        tmp = direction[0]
        direction[0] = -direction[1]
        direction[1] = tmp

    elif instruction == "R":
        tmp = direction[0]
        direction[0] = direction[1]
        direction[1] = -tmp

    count = 0

    while not check(position, grid, direction):
        count += 1
        tmp = direction[0]
        direction[0] = direction[1]
        direction[1] = -tmp

        if count == 4:
            print(position[0] - 3, position[1] - 3)
            print("DED")
            sys.exit()

    grid[position[1] - 1][position[0] - 1] = trail

    position[0] += direction[0]
    position[1] += direction[1]

    grid[position[1] - 1][position[0] - 1] = -1

    grid = update(grid)


print(position[0]-3, position[1]-3)
