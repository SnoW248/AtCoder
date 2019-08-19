N = int(input())
A = list(map(int, input().split()))

r = 0
# 分母部分を計算
for a in A:
    r += 1 / a

# 逆数を求める
result = 1 / r

print(result)
