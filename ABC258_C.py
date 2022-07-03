inputNum = list(map(int, input().split()))

N = inputNum[0]
Q = inputNum[1]
s = input()
listNum = 0
for i in range(Q):
    inputNum = list(map(int, input().split()))

    func = inputNum[0]
    x = inputNum[1]
    if func == 1:
        listNum -= x%N
    else:
        print(s[(listNum+x-1)%N])
