inputNum = list(map(int, input().split()))

W = inputNum[0]
H = inputNum[1]
x = inputNum[2]
y = inputNum[3]

maxValue = W * H / 2.000000
checkFlag = 1

if (x*2 == W):
    checkFlag = 0
    if (y*2 == H):
        checkFlag = 1

if (y*2 == H):
    checkFlag = 0
    if (x*2 == W):
        checkFlag = 1

print('{:.6f}'.format(maxValue), checkFlag)
