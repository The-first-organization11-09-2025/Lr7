def adjacency_list():
    adjacency = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [],
        4: [7],
        5: [],
        6: [8, 9],
        7: [],
        8: [],
        9: [10],
        10: []
    }
    return adjacency

def adjacency_to_path(adjacency):
    all_children = []
    for uzel in adjacency:
        children_list = adjacency[uzel]
        for child in children_list:
            all_children.append(child)
    root = 0
    for uzel in adjacency:
        in_children = False
        for child in all_children:
            if uzel == child:
                in_children = True
        if in_children == False:
            root = uzel
    path_dict = {}

    def obxod(adjacency_uzel, adjacency_path):
        if adjacency_path == '':
            materialized_path = str(adjacency_uzel)
        else:
            materialized_path = f'{adjacency_uzel}, {adjacency_path}'

        path_dict[adjacency_uzel] = materialized_path
        children = adjacency.get(adjacency_uzel, [])
        for child in children:
            obxod(child, materialized_path)
    if root != None:
        obxod(root, '')
    return path_dict

print('Исходный список смежности:')
print(adjacency_list())

print('Конвертация список смежности -> материализованный путь')
print('Полученный материализованный путь')
print(adjacency_to_path(adjacency_list()))

print()

def materialized_path():
    path = {
        1: '1',
        2: '2, 1',
        3: '3, 1',
        4: '4, 1',
        5: '5, 2, 1',
        6: '6, 2, 1',
        7: '7, 4, 1',
        8: '8, 6, 2, 1',
        9: '9, 6, 2, 1',
        10: '10, 9, 6, 2, 1'
    }
    return path

def path_to_adjacency(path):
    adjacency = {}
    uzels = list(path.keys())
    for uzel in uzels:
        materialized = path[uzel]
        parts = materialized.split(',')
        if len(parts) == 1:
            if uzel not in adjacency:
                adjacency[uzel] = []
        else:
            parent = int(parts[1])
            if parent not in adjacency:
                adjacency[parent] = []

            children = False
            for child in adjacency[parent]:
                if child == uzel:
                    children = True
            if children == False:
                adjacency[parent].append(uzel)
            if uzel not in adjacency:
                adjacency[uzel] = []
    return adjacency


print('Исходный материализованный путь')
print(materialized_path())

print('Конвертация материализованный путь -> список смежности')
print('Полученный список смежности')
print(path_to_adjacency(materialized_path()))
