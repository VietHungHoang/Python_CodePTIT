from collections import defaultdict

# Ý tưởng: Bản chất là bài toán trên đồ thị có hướng. Các tên là các đỉnh
# possible khi có đường đi tới tất cả các đỉnh (đồ thị liên thông)
# ngược lại impossible khi xảy ra 1 trường hợp vô lý trong phép so sánh hay chính là khi đồ thị tồn tại chu trình
# Tuy nhiên số lượng đỉnh trong bài toán khá lớn (10^5) trong khi thông thường sử dụng BFS, DFS thì chỉ đến 10^3
# Vì vậy nếu dùng DFS, BFS trong bài toán này chắc chắn TLE
# Do đó sử dụng thuật toán Kahn để giảm thời gian => AC

def is_possible(graph):
    adj = defaultdict(list) # Danh sách kề
    in_degree = defaultdict(int) # Lưu bán bậc vào của các đỉnh

    # Duyệt đồ thị và chuyển đồ thị dạng chữ thành danh sách kề
    for node in graph:
        a, sign, b = node.split()
        if sign == '>':
            adj[a].append(b)
            in_degree[b] += 1
        else:
            adj[b].append(a)
            in_degree[a] += 1

    queue = [node for node in adj if in_degree[node] == 0] # Lưu các đỉnh có bán bậc vào == 0
    # Duyệt tương tự BFS
    while queue:
        v = queue.pop(0)
        for x in adj[v]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                queue.append(x)

    return all(in_degree[node] == 0 for node in adj) # return True nếu tất cả các đỉnh đều đã được xoá (được duyệt)
if __name__ == '__main__':
    n = int(input())
    graph = [input() for _ in range(n)]
    print("possible" if is_possible(graph) else "impossible")
