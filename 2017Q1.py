#Sean Morrell - Aylesbury grammar school

row = list(input("Enter the first row: "))

length = len(row)

next_row = []

colours = ["R", "G", "B"]
colours2 = ["R", "G", "B"]

for j in range(1, length):
    for i in range(0, length - j):
        element1 = row[i]
        element2 = row[i+1]
        if element1 == element2:
            next_element = element1
        else:
            colours2.remove(element1)
            colours2.remove(element2)
            next_element = colours2[0]
            colours2 = colours.copy()

        next_row.append(next_element)

    if j == length-1:
        print("".join(next_row))

    row = next_row.copy()
    next_row = []
