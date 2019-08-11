inputNum = list(map(int, input().split()))

K = inputNum[0]
X = inputNum[1]

for i in range(X - K + 1, X + K):
    print(i, end=' ')
