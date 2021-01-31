#Sean Morrell - Aylesbury Grammar School

grid = [[""]*10 for _ in range(10)]

entry = input("Enter the values: ").split(" ")
a = int(entry[0])
c = int(entry[1])
m = int(entry[2])
r = 20

placed = False

for i in range(10):
    r = (a * r + c) % m

    x = r % 10

    if r < 10:
        y = 0
    else:
        y = ((r % 100) - x) // 10

    print(r, y, x)
