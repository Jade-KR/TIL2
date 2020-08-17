import sys
sys.stdin = open('숨바꼭질.txt')

def findOut(location, time):
    global minT
    if time > minT:
        return
    if location == K:
        if time < minT:
            minT = time
            return
        else:
            return

    for i in range(3):
        if i == 0:
            newL = location + 1
        elif i == 1:
            newL = location - 1
        else:
            newL = location * 2

        findOut(newL, time+1)



N, K = map(int, input().split())
minT = 987654321
t = 0

findOut(N, t)

if N == K:
    minT = 0

print(minT)