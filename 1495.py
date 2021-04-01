N, S, M = map(int, input().split())
v = list(map(int, input().split()))

result = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
result[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if result[i - 1][j] == 0:
            continue
        if j + v[i - 1] <= M:
            result[i][j + v[i - 1]] = 1
        if j - v[i - 1] >= 0:
            result[i][j - v[i - 1]] = 1
        
idx = -1
for i in range(M, -1, -1):
    if result[-1][i] == 1:
        idx = i
        break
        
print(idx)