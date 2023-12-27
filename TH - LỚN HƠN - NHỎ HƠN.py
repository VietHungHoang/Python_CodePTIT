from collections import defaultdict

def is_possible(comparisons):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for comparison in comparisons:
        a, sign, b = comparison.split()
        if sign == '>':
            graph[a].append(b)
            in_degree[b] += 1
        else:
            graph[b].append(a)
            in_degree[a] += 1
    queue = [node for node in graph if in_degree[node] == 0]
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return all(in_degree[node] == 0 for node in graph)
if __name__ == '__main__':
    n = int(input())
    comparisons = [input() for _ in range(n)]
    result = is_possible(comparisons)
    if result:
        print("possible")
    else:
        print("impossible")
    