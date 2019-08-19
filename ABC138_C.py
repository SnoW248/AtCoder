N = int(input())
V = list(map(int, input().split()))

# 低い価値のものから合成すると最大になる
V = sorted(V)
result = V[0]
for i in range(1, N):
    result = (result + V[i]) / 2

print(result)
