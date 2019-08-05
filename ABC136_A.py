inputNum = list(map(int, input().split()))

A = inputNum[0]
B = inputNum[1]
C = inputNum[2]

if ((C - (A - B)) > 0):
    print(C - (A - B))
else:
    print(0)
