alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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


def generate_graph(g, current, end, max_length, checked, depth, max_depth):
    if depth < max_depth:
        insertion = []

        for node in g:
            if node not in checked:
                vertices = generate_edges(node, max_length).copy()
                insertion.append([node, vertices].copy())
                checked.append(node)

        for insert in insertion:
            g[insert[0]] = insert[1].copy()

            if end in insert[1]:
                print("Found at depth: " + str(depth+3))
                max_depth = depth

            for vertex in insert[1]:
                if vertex not in g:
                    g[vertex] = []

        out = generate_graph(g, current, end, max_length, checked, depth+1, max_depth)
        g = out[0]
        max_depth = out[1]

    return [g, max_depth]


def main():
    graph = {"AB": []}
    target = input("Enter the desired order: ")
    length = len(target)

    graph = generate_graph(graph, "AB", target, length, [], 0, 30)[0]
    ans = dijkstra(graph, "AB", target)
    print("Minimum is: " + str(ans + 2))

    return


main()
