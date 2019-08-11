N = int(input())

s = []
dictList = []
for i in range(N):
    d = {}
    # 受け取った文字列を辞書型に{文字: 数}
    s.append(input())
    for c in s[i]:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    # 比較がしやすいようにソートしたものを追加
    dictList.append(sorted(d.items()))

count = 0
for i in range(len(dictList)):
    for j in range(i + 1, len(dictList)):
        if dictList[i] == dictList[j]:
            count += 1

print(count)
