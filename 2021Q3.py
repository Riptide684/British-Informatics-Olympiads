graph = {"AB": []}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
checked = []


def dijkstra(g, start, end):
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

    return visited[end]


def generate_edges(vertex, max_length):
    vertex_tmp = list(vertex).copy()
    neighbours = []

    #Swap
    tmp = vertex_tmp[0]
    vertex_tmp[0] = vertex_tmp[1]
    vertex_tmp[1] = tmp
    neighbours.append("".join(vertex_tmp))

    #Add
    if len(vertex) != max_length:
        new = vertex + alphabet[len(vertex)]
        neighbours.append(new)

    #Rotate
    vertex_tmp = list(vertex).copy()
    vertex_tmp.append(vertex_tmp[0])
    vertex_tmp.pop(0)
    if "".join(vertex_tmp) not in neighbours:
        neighbours.append("".join(vertex_tmp))

    return neighbours


def main():
    target = input("Enter the desired order: ")
    length = len(target)

    while len(graph) > len(checked):
        insertion = []

        for node in graph:
            if node not in checked:
                checked.append(node)
                adjacent = generate_edges(node, length).copy()
                insertion.append([adjacent, node].copy())

        for insert in insertion:
            graph[insert[1]] = insert[0].copy()

            for node in insert[0]:
                if node not in graph:
                    graph[node] = []

    quickest = dijkstra(graph, "AB", target)
    print(quickest + 2)

    return


main()
