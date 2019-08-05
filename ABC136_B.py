N = int(input())

numOfDigit = 1
answer = 0

# 最大桁より下の桁で桁数が奇数の個数
n = 1
while(N >= n * 10):
    if (numOfDigit % 2):
        answer += n * 9
    numOfDigit += 1
    n *= 10

# 最大桁が奇数の場合
if (numOfDigit % 2):
    answer += N % (n * 10) - n + 1

print(answer)
