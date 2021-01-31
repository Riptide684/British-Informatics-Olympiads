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


def move(current, end, checked, minimum, length, depth):
    vertices = generate_edges(current, length)
    for vertex in vertices:
        if vertex not in checked and depth < minimum:
            if vertex == end:
                minimum = depth
            else:
                checked = checked.copy()
                checked.append(vertex)
                minimum = move(vertex, end, checked, minimum, length, depth+1)

    return minimum


def main():
    target = input("Enter the desired order: ")
    out = move("AB", target, ["AB"], 25, len(target), 2)
    print(out+1)
    return


main()
