N = int(input())
H = list(map(int, input().split()))

yesFlag = True

# 基本的に低くする
# 次のマスが今のマスより低いと単調増加にならない
for i in range(len(H) - 1):
    if (H[i + 1] - H[i] > 0):
        H[i + 1] -= 1
    elif (H[i + 1] - H[i] < 0):
        yesFlag = False

if (yesFlag):
    print('Yes')
else:
    print('No')
