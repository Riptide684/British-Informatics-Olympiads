tiles = {
    "1": ["NS", "EW"],
    "2": ["EW", "NS"],
    "3": ["NW", "ES"],
    "4": ["NE", "SW"],
    "5": ["ES", "NW"],
    "6": ["SW", "NE"]
}

directions = {
    "N": [0, -1],
    "S": [0, 1],
    "E": [1, 0],
    "W": [-1, 0]
}

opposites = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E"
}

size = int(input("Enter grid size: "))
grid = []

for i in range(size):
    row = input("Enter the row: ").split(" ")
    grid.append(row)

red = 0
green = 0

red_tracks = []
green_tracks = []

for i in range(size):
    red_row = []
    green_row = []

    for j in range(size):
        red_row.append(tiles[grid[i][j]][0])
        green_row.append(tiles[grid[i][j]][1])

    red_tracks.append(red_row)
    green_tracks.append(green_row)

checked = []

for y in range(1, size + 1):
    rows = red_tracks[y-1]
    for x in range(1, size + 1):
        if [x, y] not in checked:
            track = rows[x-1]
            direction = directions[track[0]]
            new_coords = [x + direction[0], y + direction[1]]
            count = 1
            way = track[0]
            checked.append([x, y])

            while 0 < new_coords[0] <= size and 0 < new_coords[1] <= size and new_coords not in checked:
                if opposites[way] in red_tracks[new_coords[1]-1][new_coords[0]-1]:
                    new = new_coords.copy()
                    checked.append(new)

                    count += 1

                    if red_tracks[new_coords[1]-1][new_coords[0]-1].index(opposites[way]) == 1:
                        new_direction = red_tracks[new_coords[1]-1][new_coords[0]-1][0]
                    else:
                        new_direction = red_tracks[new_coords[1] - 1][new_coords[0] - 1][1]

                    way = new_direction
                    new_coords[0] += directions[new_direction][0]
                    new_coords[1] += directions[new_direction][1]

                    if new_coords[0] == x and new_coords[1] == y:
                        red += count
                        break

                else:
                    break

checked = []

for y in range(1, size + 1):
    rows = green_tracks[y-1]
    for x in range(1, size + 1):
        if [x, y] not in checked:
            track = rows[x-1]
            direction = directions[track[0]]
            new_coords = [x + direction[0], y + direction[1]]
            count = 1
            way = track[0]
            checked.append([x, y])

            while 0 < new_coords[0] <= size and 0 < new_coords[1] <= size and new_coords not in checked:
                if opposites[way] in green_tracks[new_coords[1]-1][new_coords[0]-1]:
                    new = new_coords.copy()
                    checked.append(new)

                    count += 1

                    if green_tracks[new_coords[1]-1][new_coords[0]-1].index(opposites[way]) == 1:
                        new_direction = green_tracks[new_coords[1]-1][new_coords[0]-1][0]
                    else:
                        new_direction = green_tracks[new_coords[1] - 1][new_coords[0] - 1][1]

                    way = new_direction
                    new_coords[0] += directions[new_direction][0]
                    new_coords[1] += directions[new_direction][1]

                    if new_coords[0] == x and new_coords[1] == y:
                        green += count
                        break

                else:
                    break

print(red)
print(green)
