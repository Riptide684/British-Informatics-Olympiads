#Sean Morrell - Aylesbury Grammar School

promenade = list(input("Enter the promenade: "))

fraction = [1, 1]
right = [0, 1]
left = [1, 0]

for letter in promenade:
    if letter == "L":
        left = fraction.copy()
    elif letter == "R":
        right = fraction.copy()
    else:
        print("Invalid promenade")

    fraction[0] = left[0] + right[0]
    fraction[1] = left[1] + right[1]

print(str(fraction[0]) + " / " + str(fraction[1]))
