#Sean Morrell - Aylesbury Grammar School

size = 100

grid = [[0]*size for _ in range(size)]

entry = input("Enter the three integers: ")

entry = entry.split(" ")

position = int(entry[0])
sequence_size = int(entry[1])
turns = int(entry[2])

overflow = False

sequence = input("Enter the sequence separated by spaces: ")

sequence = sequence.split(" ")

for j in range(1, turns+1):
    row = (position-1) // 5
    column = (position % 5) - 1
    if column == 0:
        column = 4

    target_row = size//2 - 1 + row
    target_column = size//2 - 1 + column

    grid[target_row][target_column] += 1

    if grid[size//2-1+row][size//2-1+column] >= 4:
        overflow = True
        location = [size//2-1+row, size//2-1+column]

        while overflow:
            grid[location[0]][location[1]] -= 4         #reset square
            grid[location[0]-1][location[1]] += 1       #up
            grid[location[0]+1][location[1]] += 1       #down
            grid[location[0]][location[1]-1] += 1       #left
            grid[location[0]][location[1]+1] += 1       #right

            overflow = False

            for y in range(size):                   #check for overflows
                for x in range(size):
                    if grid[y][x] >= 4:
                        overflow = True
                        location = [y, x]

    position = (position + int(sequence[(j-1) % sequence_size])) % 25

board = ""

for n in range(5):
    for m in range(5):
        board += str(grid[size//2 + n - 1][size//2 + m - 1]) + " "

    board += "\n"

print(board)
