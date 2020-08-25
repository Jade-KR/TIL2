import sys
sys.stdin = open("터널의 입구와 출구.txt")

def check(e, o):
    global cars, flag, max_c
    cars += e
    cars -= o
    if cars < 0:
        flag = 1
        max_c = 0
        return
    else:
        if cars > max_c:
            max_c = cars




n = int(input())
cars = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
max_c = -987654321
flag = 0

for i in range(n):
    if flag != 1:
        check(data[i][0], data[i][1])

print(max_c)