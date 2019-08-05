n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

maxCount = 0
for i in range(0, n):
    # i番目の敵をできるだけ倒す
    if a[i] > b[i]:
        maxCount += b[i]
        continue
    else:
        maxCount += a[i]
        b[i] -= a[i]
    # i+1番目の敵をできるだけ倒す
    if a[i + 1] > b[i]:
        maxCount += b[i]
        a[i + 1] -= b[i]
    else:
        maxCount += a[i + 1]
        a[i + 1] = 0

print(maxCount)
