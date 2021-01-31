import math


def npr(n, r, repeats):
    bottom = 1
    for i in range(len(repeats)):
        bottom *= math.factorial(repeats[i])

    ans = math.factorial(n) // (math.factorial(n-r) * bottom)
    return ans


def partition(num, partitions, total, depth, mini, maxi, lengths, arr, tmp):
    for i in range(mini, num+1):
        tmp = tmp.copy()
        tmp.append(i)
        total += i

        if i > maxi:
            break

        if total == num:
            partitions += 1
            lengths[depth-1] += 1
            arr.append(tmp.copy())
            break

        elif total > num:
            break

        out = partition(num, partitions, total, depth+1, i, maxi, lengths, arr, tmp)
        partitions = out[0]
        lengths = out[1]
        arr = out[2]
        total -= i
        tmp = tmp[:-1]

    return [partitions, lengths, arr]


def main():
    entries = input("Enter the values: ").split(" ")
    number = int(entries[3])
    m = int(entries[1])
    items = int(entries[2])
    parcels = int(entries[0])

    ways = partition(number, 0, 0, 1, 1, m, [0]*number, [], [])[1]
    summation = 0
    arrangements = partition(items, 0, 0, 1, 1, number, [0]*items, [], [])
    exact_arrangements = arrangements[2]
    configurations = []

    for exact_arrangement in exact_arrangements:
        if len(exact_arrangement) == parcels:
            configurations.append(exact_arrangement.copy())

    for i in range(len(configurations)):
        product = 1
        configuration = configurations[i]
        numbers = []
        for j in range(parcels):
            product *= ways[configuration[j]-1]
            numbers.append(configuration[j])

        dic = {}

        for letter in numbers:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1

        repeated = []

        for elements in dic:
            repeated.append(dic[elements])

        product *= npr(parcels, parcels, repeated)

        summation += product

    print(summation)

    return


main()
