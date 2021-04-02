import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visit[v] = True
    for e in graph[v]:
        if not visit[e]:
            dfs(e)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

visit = [False] * (N+1)

count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(1,N+1):
    if not visit[j]:
        dfs(j)
        count += 1
        
print(count)
