import sys
from collections import deque


def read_input():
    input = sys.stdin.read().splitlines()
    idx = 0
    test_cases = []
    while idx < len(input):
        N, M, T = map(int, input[idx].split())
        if N == 0 and M == 0 and T == 0:
            break
        idx += 1
        maze = []
        for _ in range(N):
            maze.append(input[idx])
            idx += 1
        test_cases.append((N, M, T, maze))
    return test_cases


def get_min_distance(N, M, maze, door_pos):
    min_dist = [[-1 for _ in range(M)] for _ in range(N)]
    queue = deque()
    door_x, door_y = door_pos
    queue.append((door_x, door_y))
    min_dist[door_x][door_y] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N
                and 0 <= ny < M
                and maze[nx][ny] != "X"
                and min_dist[nx][ny] == -1
            ):
                min_dist[nx][ny] = min_dist[x][y] + 1
                queue.append((nx, ny))
    return min_dist


def solve_case(N, M, T, maze):
    # Locate start and door positions
    start = door = None
    for i in range(N):
        for j in range(M):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "D":
                door = (i, j)
    if not start or not door:
        return "NO"

    min_dist = get_min_distance(N, M, maze, door)
    start_x, start_y = start
    door_x, door_y = door

    if min_dist[start_x][start_y] == -1:
        return "NO"

    # Precompute cell indices for bitmask
    cell_indices = {}
    index = 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] != "X":
                cell_indices[(i, j)] = index
                index += 1
    total_cells = index

    # If T is less than min_dist, impossible
    if min_dist[start_x][start_y] > T:
        return "NO"

    # If T is greater than total_cells, impossible (since can't revisit)
    if T > total_cells:
        return "NO"

    # Initialize the starting state
    start_pos = start_x * M + start_y
    start_mask = 1 << cell_indices[start]
    current_x = [start_x]
    current_y = [start_y]
    current_mask = [start_mask]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for t in range(1, T + 1):
        next_x = []
        next_y = []
        next_mask = []
        for i in range(len(current_x)):
            x = current_x[i]
            y = current_y[i]
            mask = current_mask[i]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != "X":
                    pos = cell_indices.get((nx, ny), -1)
                    if pos == -1:
                        continue
                    if not (mask & (1 << pos)):
                        remaining_time = T - t
                        if (
                            min_dist[nx][ny] != -1
                            and min_dist[nx][ny] <= remaining_time
                        ):
                            new_mask = mask | (1 << pos)
                            next_x.append(nx)
                            next_y.append(ny)
                            next_mask.append(new_mask)
        if not next_x:
            return "NO"
        current_x, current_y, current_mask = next_x, next_y, next_mask

    # Check if any state is at the door position
    for i in range(len(current_x)):
        if current_x[i] == door_x and current_y[i] == door_y:
            return "YES"
    return "NO"


def main():
    test_cases = read_input()
    results = []
    for case in test_cases:
        N, M, T, maze = case
        result = solve_case(N, M, T, maze)
        results.append(result)
    print("\n".join(results))


if __name__ == "__main__":
    main()
