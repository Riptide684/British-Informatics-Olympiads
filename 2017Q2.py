#Sean Morrell - Aylesbury Grammar School


symbol = {
    1: "x",
    2: "o"
}


def generate_moves(pos):
    moves = ["up", "down", "right", "left"]

    if pos <= 6:
        moves.remove("up")
    if pos > 30:
        moves.remove("down")
    if pos % 6 == 1:
        moves.remove("left")
    if pos % 6 == 0:
        moves.remove("right")

    return moves


def check_moves(board, pos, pos_moves):
    if pos % 6 == 0:
        adjust = 1
    else:
        adjust = 0

    if "up" in pos_moves:
        if board[11 * (pos//6) - 7 + pos % 6 - 5 * adjust] != "":
            pos_moves.remove("up")

    if "right" in pos_moves:
        if board[11 * (pos//6) + pos % 6 - 1] != "":
            pos_moves.remove("right")

    if "left" in pos_moves:
        if board[11 * (pos//6) + pos % 6 - 2 - 5 * adjust] != "":
            pos_moves.remove("left")

    if "down" in pos_moves:
        if board[11 * (pos//6) + pos % 6 + 4 - 5 * adjust] != "":
            pos_moves.remove("down")

    if turn == 1:
        if "up" in pos_moves:
            return "up"

        elif "right" in pos_moves:
            return "right"

        elif "down" in pos_moves:
            return "down"

        elif "left" in pos_moves:
            return "left"

    elif turn == 2:
        if "up" in pos_moves:
            return "up"

        elif "left" in pos_moves:
            return "left"

        elif "down" in pos_moves:
            return "down"

        elif "right" in pos_moves:
            return "right"

    return "skip"


def make_move(board, pos, direction):
    if pos % 6 == 0:
        adjust = 1
    else:
        adjust = 0

    if direction == "up":
        board[11 * (pos//6) - 7 + pos % 6 - 5 * adjust] = "|"
        return board

    elif direction == "right":
        board[11 * (pos//6) + pos % 6 - 1] = "|"
        return board

    elif direction == "left":
        board[11 * (pos//6) + pos % 6 - 2 - 5 * adjust] = "|"
        return board

    elif direction == "down":
        board[11 * (pos//6) + pos % 6 + 4 - 5 * adjust] = "|"
        return board


def check_squares(board):
    points = 0
    n = 0
    count = 1

    for j in range(25):
        if board[n] == "|":
            if board[n+11] == "|":
                if board[n+6] == "|":
                    if board[n+5] == "|":
                        if j not in captured:
                            captured.append(j)
                            if turn == 1:
                                crosses.append(j)
                            else:
                                noughts.append(j)
                            points += 1

        n += 1
        if count % 5 == 0:
            n += 6

        count += 1

    return points


position1 = int(input("Enter position 1: "))
modifier1 = int(input("Enter modifier 1: "))
position2 = int(input("Enter position 2: "))
modifier2 = int(input("Enter modifier 2: "))
turns = int(input("Enter the number of turns: "))

turn = 1

points1 = 0
points2 = 0
points_old = 0
noughts = []
crosses = []
captured = []

grid = [""] * 60

for i in range(turns):
    if turn == 1:
        position1 = (position1 + modifier1) % 36
        if position1 == 0:
            position1 = 36

        possible_moves = generate_moves(position1)
        move = check_moves(grid, position1, possible_moves)
        while move == "skip":
            position1 = (position1 + 1) % 36
            if position1 == 0:
                position1 = 36

            possible_moves = generate_moves(position1)
            move = check_moves(grid, position1, possible_moves)

        grid = make_move(grid, position1, move)

        points_new = check_squares(grid)

        if points_new == points_old:
            turn = 2

    elif turn == 2:
        position2 = (position2 + modifier2) % 36

        if position2 == 0:
            position2 = 36

        possible_moves = generate_moves(position2)
        move = check_moves(grid, position2, possible_moves)
        while move == "skip":
            position2 = (position2 + 1) % 36
            if position2 == 0:
                position2 = 36

            possible_moves = generate_moves(position2)
            move = check_moves(grid, position2, possible_moves)

        grid = make_move(grid, position2, move)

        points_new = check_squares(grid)

        if points_new == points_old:
            turn = 1

points1 = len(crosses)
points2 = len(noughts)

final_grid = []

for k in range(25):
    if k in crosses:
        final_grid.append("X")
    elif k in noughts:
        final_grid.append("O")
    else:
        final_grid.append("*")

    final_grid.append(" ")

    if k % 5 == 4:
        final_grid.append("\n")

print("".join(final_grid))
print(points1, points2)
