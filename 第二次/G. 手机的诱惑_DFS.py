# 定义方向向量，用于上下左右移动
mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]


def check_reachable(end_x, end_y, n, m, graph):
    """
    使用广度优先搜索（BFS）计算从终点到各点的最短路径。
    """
    reachable = [[0 for _ in range(m)] for _ in range(n)]
    queue = [(end_x, end_y, 1)]
    reachable[end_x][end_y] = 1

    while queue:
        x, y, time = queue.pop(0)
        for i in range(4):
            nx, ny = x + mx[i], y + my[i]
            # 检查新的坐标是否在边界内，且没有被访问过
            if (
                0 <= nx < n
                and 0 <= ny < m
                and graph[nx][ny] != "X"
                and reachable[nx][ny] == 0
            ):
                reachable[nx][ny] = time + 1
                queue.append((nx, ny, time + 1))
    return reachable


def dfs(x, y, time, n, m, t, graph, end_x, end_y, reachable, can_out):
    """
    使用深度优先搜索（DFS）从起点遍历到终点，在有限时间内判断是否可达。
    """
    if can_out[0]:  # 如果已经找到解，直接返回
        return
    if time == t:
        if x == end_x and y == end_y:
            can_out[0] = True
        return
    if reachable[x][y] - 1 > t - time:  # 如果剩余时间不足以到达终点，剪枝
        return

    for i in range(4):
        nx, ny = x + mx[i], y + my[i]
        # 确保新的坐标在边界内，且不是障碍物或起点
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in ["X", "S"]:
            graph[x][y] = "X"  # 暂时标记为障碍物，防止重复访问
            dfs(nx, ny, time + 1, n, m, t, graph, end_x, end_y, reachable, can_out)
            graph[x][y] = "."  # 还原为可通行路径


while True:
    try:
        N, M, T = map(int, input().split())  # 输入网格尺寸和最大时间
    except EOFError:
        break

    if N == 0 and M == 0 and T == 0:
        break

    # 初始化图形矩阵
    maze = [list(input().strip()) for _ in range(N)]

    start = None
    end = None

    # 记录起点和终点的位置
    for i in range(N):
        for j in range(M):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "D":
                end = (i, j)

    start_x, start_y = start
    end_x, end_y = end

    # 奇偶性剪枝：如果起点和终点的奇偶性不同且步数不合适，直接判断不可达
    if (end_x + end_y + start_x + start_y) % 2 != T % 2:
        print("NO")
        continue

    # 计算从终点的可达路径
    reachable = check_reachable(end_x, end_y, N, M, maze)

    # 判断起点是否可达终点
    if reachable[start_x][start_y] == 0:
        print("NO")
        continue

    # 判断网格中可用的空格是否足够大于时间限制
    cnt_wall = sum(row.count("X") for row in maze)
    if N * M - cnt_wall <= T:
        print("NO")
        continue

    # 使用 DFS 进行可达性判断
    can_out = [False]
    dfs(start_x, start_y, 0, N, M, T, maze, end_x, end_y, reachable, can_out)
    print("YES" if can_out[0] else "NO")
