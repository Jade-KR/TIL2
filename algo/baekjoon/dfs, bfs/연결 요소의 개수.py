import sys, collections
sys.stdin = open('연결 요소의 개수.txt')

def bfs(v):
    global cnt
    q = collections.deque()
    q.append(v)
    while len(q):
        t = q.popleft()

        for w in range(1, N+1):
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)



N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
visited = [0 for _ in range(N+1)]

adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
cnt = 0

for i in range(M):
    adj[data[i][0]][data[i][1]] = 1
    adj[data[i][1]][data[i][0]] = 1


for i in range(M):
    for j in range(2):
        if visited[data[i][j]] != 1:
            bfs(data[i][j])
            cnt += 1

print(cnt)