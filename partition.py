import math


def check_prime(n):
    if n == 1:
        return False

    x = 2
    y = 2
    d = 1

    while d == 1:
        x = (x ** 2 + 1) % n
        y = (((y ** 2 + 1) % n) ** 2 + 1) % n
        d = math.gcd(abs(x - y), n)

    if d == n or d == 1:
        return True
    else:
        return False


with open("primes.txt", "a+") as f:
    for i in range(2, 500000):
        if check_prime(2 * i - 1):
            f.write(str(2 * i - 1) + "\n")
