N = int(input())

s = ''.join(sorted(input()))
h = {s: 1}
count = 0
for i in range(N - 1):
    # 比較がしやすいようにソートしたものを追加
    s = ''.join(sorted(input()))
    if s in h:
        count += h[s]
        h[s] += 1
    else:
        h[s] = 1

print(count)
