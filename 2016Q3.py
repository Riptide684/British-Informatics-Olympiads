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


def generate_primes(n, limit):
    below = math.floor(math.log(n-1, 2))
    above = math.floor(math.log(limit-n, 2))

    primes = []

    for i in range(below+1):
        test = n - pow(2, i)
        if check_prime(test):
            primes.append(test)

    for j in range(above+1):
        test = n + pow(2, j)
        if check_prime(test):
            primes.append(test)

    return primes


def move(g, beginning, target):
    nodes = []
    for node in g:
        nodes.append(node)

    distances = {}

    for node in nodes:
        children = g[node]
        row = {}
        for child in children:
            row[child] = 1

        distances[node] = row

    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = beginning
    current_distance = 0
    unvisited[current] = current_distance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

    return visited[target]


entries = input("Enter the values: ").split(" ")
bound = int(entries[0])
start = int(entries[1])
end = int(entries[2])
graph = {start: []}
checked = []


def main():
    while len(graph) > len(checked):
        insertion = []
        for vertex in graph:
            if vertex not in checked:
                checked.append(vertex)
                insertion.append([vertex, generate_primes(vertex, bound).copy()].copy())

        for insert in insertion:
            graph[insert[0]] = insert[1].copy()
            for node in insert[1]:
                if node not in graph:
                    graph[node] = []

    print(move(graph, start, end)+1)

    return


main()
