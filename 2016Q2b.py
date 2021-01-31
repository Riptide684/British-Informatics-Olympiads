#Sean Morrell - Aylesbury Grammar School


def pos_to_coords(pos):
    coordinates = [0, 0]
    y = 5 - ((pos - 1) // 5)
    x = pos % 5
    if x == 0:
        x = 5

    coordinates[0] = x
    coordinates[1] = y

    return coordinates


def do_overflow(board):
    add = []

    for element in board:
        if board[element] >= 4:
            board[element] -= 4

            coordinate = element.strip('][').split(', ')
#####################################################################
            coordinate1 = [0, 0]
            coordinate1[0] = int(coordinate[0]) + 1
            coordinate1[1] = int(coordinate[1])

            if str(coordinate1) in board:
                board[str(coordinate1)] += 1
            else:
                add.append(coordinate1)
#####################################################################
            coordinate2 = [0, 0]
            coordinate2[0] = int(coordinate[0]) - 1
            coordinate2[1] = int(coordinate[1])

            if str(coordinate2) in board:
                board[str(coordinate2)] += 1
            else:
                add.append(coordinate2)
#####################################################################
            coordinate3 = [0, 0]
            coordinate3[0] = int(coordinate[0])
            coordinate3[1] = int(coordinate[1]) + 1

            if str(coordinate3) in board:
                board[str(coordinate3)] += 1
            else:
                add.append(coordinate3)
#####################################################################
            coordinate4 = [0, 0]
            coordinate4[0] = int(coordinate[0])
            coordinate4[1] = int(coordinate[1]) - 1

            if str(coordinate4) in board:
                board[str(coordinate4)] += 1
            else:
                add.append(coordinate4)
#####################################################################
    for value in add:
        board[str(value)] = 1

    check = False

    for element in board:
        if board[element] >= 4:
            check = True

    return[board, check]


entry = input("Enter the values: ")
values = entry.split(" ")
position = int(values[0])
sequence_length = int(values[1])
turns = int(values[2])
sequence = input("Enter the sequence: ").split(" ")

grid = {}

for i in range(turns):
    coords = pos_to_coords(position)

    if str(coords) in grid:
        grid[str(coords)] += 1
    else:
        grid[str(coords)] = 1

    if grid[str(coords)] >= 4:
        overflow = True

        while overflow:
            tmp = do_overflow(grid)
            grid = tmp[0]
            overflow = tmp[1]

    position = (position + int(sequence[i % sequence_length])) % 25

    if position == 0:
        position = 25

output = ""

for a in range(1, 6):
    for b in range(1, 6):
        try:
            number = grid["[" + str(b) + ", " + str(6-a) + "]"]
        except KeyError:
            number = 0

        output += str(number) + " "

    output += "\n"

print(output)
print(grid)
