alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

entries = input("Enter the values: ").split(" ")
length = int(entries[0])
word = list(entries[1])
order = 1
maximum = 99

for i in range(len(word)):
    letter = word[i]

    for j in range(1, len(word)-i):
        new_letter = word[j+i]
        if alphabet.index(new_letter) > alphabet.index(letter):
            if alphabet.index(new_letter) < maximum:
                maximum = alphabet.index(new_letter)

            order += 1

done = False

if order != 1:
    if maximum != length - 1:
        print(0)
        done = True

    else:
        length -= 1
        word.remove(alphabet[maximum])

first = 99

if not done:
    for i in range(len(word)):
        letter = word[i]
        if alphabet.index(letter) < first:
            first = alphabet.index(letter)

    print(first)
