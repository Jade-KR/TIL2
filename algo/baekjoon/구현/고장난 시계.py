import sys
sys.stdin = open("고장난 시계.txt")

h, m = map(int, input().split())

nm = (h%30) * 12


if nm == m:
    print('O')
else:
    print('X')