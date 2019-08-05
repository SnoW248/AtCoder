inputNum = list(map(int, input().split()))
L = list(map(int, input().split()))

N = inputNum[0]
X = inputNum[1]

D = [0]
# 座標0を含める
count = 1

for i, l in enumerate(L):
    # D[i+1]を求める
    D.append(D[i] + l)
    if(D[i+1] <= X):
        count += 1
    else:
        break

print(count)
