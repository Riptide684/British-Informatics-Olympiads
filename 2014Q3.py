import math


def ncr(n, r):
    ans = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
    return ans


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
size = len(alphabet)

number = int(input("Enter the number: "))

length = 0
total = 0
add = 0

while total < number:
    length += 1
    add = ncr(size, length)
    total += add

new_number = number - total + add
letters = []
tmp = 0

for i in range(1, length + 1):
    total = 0
    count = 0

    while total < new_number:
        count += 1
        add = ncr(size-count-tmp, length-i)
        total += add

    new_number = new_number - total + add
    letters.append(alphabet[count-1+tmp])
    tmp = count + tmp

print("".join(letters))
