import sys
sys.stdin = open('연결 요소의 개수.txt')
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        t = q.popleft()

        for w in data[t]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)

N, M = map(int, input().split())
data = [[]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
c = 0

for i in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        c += 1
        bfs(i)

print(c)