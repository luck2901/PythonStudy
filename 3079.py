import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maxVal = 0

v=[int(input())for _ in range(N)]
result = 0
left = 0
right = M * max(v)

while left <= right:
    mid = (left + right) // 2
    
    judgedPeople = 0
    for t in v:
        judgedPeople += mid // t
    
    if judgedPeople < M:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
        
print(result)