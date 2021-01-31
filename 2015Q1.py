#Sean Morrell - Aylesbury Grammar School

word1 = list(input("Enter the word: "))

counter = 0


def block(word, count):
    for n in range(1, (len(word) // 2) + 1):
        first_block = word[0:n]
        second_block = word[len(word)-n:len(word)]

        if first_block == second_block:
            count += 1
            try:
                new_word = word[n:-n]
                count = block(new_word, count)
            except IndexError:
                pass

    return count


counter = block(word1, counter)
print(counter)
