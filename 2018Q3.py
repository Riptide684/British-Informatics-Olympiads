digits = int(input("Enter the number of digits: "))
number = input("Enter the serial number: ")

graph = {number: []}
checked = []


def generate_serials(num):
    num = list(num)
    serials = []
    for i in range(len(num)-1):
        first = int(num[i])
        second = int(num[i+1])

        if i == 0:
            left = 0
            right = int(num[2])
        elif i == len(num)-2:
            left = int(num[i-1])
            right = 0
        else:
            right = int(num[i+2])
            left = int(num[i-1])

        if first < left < second or first > left > second or first < right < second or first > right > second:
            serial = num.copy()
            serial[i] = str(second)
            serial[i+1] = str(first)
            serials.append("".join(serial))

    return serials


def move(g, start):
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
    current = start
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

    return visited


def main():
    #Generate graph
    insertion = []

    while len(graph) > len(checked):
        for vertex in graph:
            if vertex not in checked:
                insertion.append([vertex, generate_serials(vertex).copy()].copy())
                checked.append(vertex)
        for insert in insertion:
            graph[insert[0]] = insert[1].copy()
            for node in insert[1]:
                if node not in graph:
                    graph[node] = []

    #Traverse graph
    maxi = 0
    distances = move(graph, number)
    for distance in distances:
        length = distances[distance]
        if length > maxi:
            maxi = length

    print(maxi)

    return


main()
