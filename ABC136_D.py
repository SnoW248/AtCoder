S = input()

count = 1
answer = [0] * len(S)
# RLの切り替わるインデックスをマーク
n = 0
for i in range(len(S) - 1):
    if (S[i] == S[i + 1]):
        count += 1
    else:
        if (S[i + 1] == 'R'):
            # Lを割り振る
            answer[n] += count // 2
            answer[n + 1] += -(-count // 2)
            count = 1
        else:
            # Rを割り振る
            answer[i] += -(-count // 2)
            answer[i + 1] += count // 2
            count = 1
            n = i
    # 右端のLを割り振る
    if (i == len(S) - 2):
        answer[n] += count // 2
        answer[n + 1] += -(-count // 2)

for i, c in enumerate(answer):
    print(c, end='')
    print(' ', end='')
