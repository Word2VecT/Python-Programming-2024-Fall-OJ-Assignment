import sys
import sys
import sys
from collections import deque


class HopcroftKarp:
    def __init__(self, graph, N, M):
        self.N = N  # Number of nodes on left side (rows)
        self.M = M  # Number of nodes on right side (columns)
        self.graph = graph  # Adjacency list for left nodes
        self.pair_U = [0] * (N + 1)
        self.pair_V = [0] * (M + 1)
        self.dist = [0] * (N + 1)

    def bfs(self):
        queue = deque()
        for u in range(1, self.N + 1):
            if self.pair_U[u] == 0:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("inf")
        self.dist[0] = float("inf")
        while queue:
            u = queue.popleft()
            if u != 0:
                for v in self.graph[u]:
                    if self.dist[self.pair_V[v]] == float("inf"):
                        self.dist[self.pair_V[v]] = self.dist[u] + 1
                        queue.append(self.pair_V[v])
        return self.dist[0] != float("inf")

    def dfs(self, u):
        if u != 0:
            for v in self.graph[u]:
                if self.dist[self.pair_V[v]] == self.dist[u] + 1:
                    if self.dfs(self.pair_V[v]):
                        self.pair_U[u] = v
                        self.pair_V[v] = u
                        return True
            self.dist[u] = float("inf")
            return False
        return True

    def max_matching(self):
        matching = 0
        while self.bfs():
            for u in range(1, self.N + 1):
                if self.pair_U[u] == 0:
                    if self.dfs(u):
                        matching += 1
        return matching


def readints():
    import sys

    return list(map(int, sys.stdin.readline().split()))


def main():
    test_case = 1
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        parts = line.strip().split()
        if not parts:
            continue
        N, M, K = map(int, parts)
        edges = []
        graph = [[] for _ in range(N + 1)]
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            edges.append((x, y))
            graph[x].append(y)
        # Compute initial maximum matching
        hk = HopcroftKarp(graph, N, M)
        S = hk.max_matching()
        C = 0
        for idx in range(K):
            x, y = edges[idx]
            # Remove edge (x,y)
            graph[x].remove(y)
            # Recompute maximum matching
            hk_temp = HopcroftKarp(graph, N, M)
            S_temp = hk_temp.max_matching()
            if S_temp < S:
                C += 1
            # Add edge back
            graph[x].append(y)
        print(f"Board {test_case} have {C} important blanks for {S} chessmen.")
        test_case += 1


if __name__ == "__main__":
    main()
