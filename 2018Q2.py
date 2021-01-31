#Sean Morrell - Aylesbury Grammar School

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cipher = []

entry = input("Input the values: ")
values = entry.split(" ")
jump = int(values[0])
plaintext = list(values[1])

position = 0

for i in range(26):
    position = (position + jump) % len(alphabet)
    letter = alphabet[position - 1]
    alphabet.remove(letter)
    if position != 0:
        position -= 1
    cipher.append(letter)

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

ciphertext = ""

count = 0

for character in plaintext:
    new_letter = cipher[(alphabet.index(character) + count) % 26]
    ciphertext += new_letter
    count += 1

print("".join(cipher[0:6]))
print(ciphertext)
