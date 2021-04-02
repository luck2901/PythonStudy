import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())

start = N // 5

tag = False

for i in range(start, -1, -1):
    tmp = N - i * 5
    if tmp % 3 == 0:
        print(int(i + tmp / 3))
        tag = True
        break

if tag == False:
    print(-1)