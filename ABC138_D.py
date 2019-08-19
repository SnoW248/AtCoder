inputNumN = list(map(int, input().split()))
N = inputNumN[0]
Q = inputNumN[1]

# 根付き木の状態を辞書型で表現する
# {int(根): int[](木)}で表現
AB = {}
for i in range(N - 1):
    inputNumAB = list(map(int, input().split()))
    if not AB.get(inputNumAB[0]):
        AB[inputNumAB[0]] = []
    AB[inputNumAB[0]].append(inputNumAB[1])

# 根のカウンターの値にxを足す
result = [0] * N
for i in range(Q):
    inputNumPQ = list(map(int, input().split()))
    result[inputNumPQ[0] - 1] += inputNumPQ[1]

# 木に根のカウンターの値を加える
for A, B in AB.items():
    for b in B:
        result[b - 1] += result[A - 1]

print(*result)
