from collections import defaultdict, deque


def dfs(graph, start, path):
    stack = [start]
    while stack:
        current_vertex = stack[-1]
        if graph[current_vertex]:
            next_vertex = graph[current_vertex].pop()
            stack.append(next_vertex)
        else:
            path.append(stack.pop())


def find_eulerian_path_or_cycle(edges):
    degrees = defaultdict(int)
    graph = defaultdict(list)
    
    # Построение графа и подсчёт степеней вершин
    for u, v in edges:
        graph[u].append(v)
        degrees[u] += 1
        degrees[v] -= 1
        
    # Поиск стартовой вершины
    odd_degree_vertices = [v for v, d in degrees.items() if abs(d) > 0]
    if len(odd_degree_vertices) > 2:
        return None
    elif len(odd_degree_vertices) == 2:
        start_vertex = odd_degree_vertices[0]
    else:
        start_vertex = min(degrees.keys())  # Можно начать с любого узла, если цикл замкнутый
    
    # DFS для нахождения Эйлерова пути/цикла
    path = []
    dfs(graph, start_vertex, path)
    
    # Возвращаем обратный порядок пути
    return path[::-1]


def can_chain(dominoes):
    if not dominoes:
        return []
    
    # Преобразование костяшек домино в рёбра графа
    edges = [(u, v) for u, v in dominoes]
    
    eulerian_path = find_eulerian_path_or_cycle(edges)
    if eulerian_path is None:
        return None
    
    # Формируем итоговую последовательность домино
    result = []
    prev_vertex = None
    for vertex in eulerian_path[:-1]:  # Исключаем последнюю вершину
        if prev_vertex is not None:
            matching_domino = next((d for d in dominoes if sorted([prev_vertex, vertex]) == sorted(d)), None)
            if matching_domino is None:
                return None
            
            # Ориентируем костяшку правильно
            if matching_domino[0] == prev_vertex:
                result.append(matching_domino)
            else:
                result.append((matching_domino[1], matching_domino[0]))
        
        prev_vertex = vertex
    
    return result


# Тестовые случаи
if __name__ == "__main__":
    print(can_chain([]))                      # Должно вернуть пустой список
    print(can_chain([(1, 1)]))               # Должно вернуть [(1, 1)]
    print(can_chain([(1, 2)]))               # Нет правильного решения
    print(can_chain([(1, 2), (3, 1), (2, 3)])) # Должно вернуть одну из возможных правильных последовательностей