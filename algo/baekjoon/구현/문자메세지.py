import sys
sys.stdin = open('문자메세지.txt')


def check(t):
    global time, prev_key
    for i in range(1, 10):
        if t in key[i]:
            current_key = i
            break

    if prev_key == current_key and current_key != 1:
        time += w

    prev_key = current_key
    time += (key[current_key].index(t)+1)*p

p, w = map(int, input().split())
text = list(input())
prev_key = 0
time = 0

key = {
    1: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']
}

for k in text:
    check(k)

print(time)