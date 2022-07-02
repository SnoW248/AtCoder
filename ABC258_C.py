def func_1(s:str, x: int):
    for _ in range(x):
        s = s[-1] + s[0:-1]
    
    return s


def func_2(s:str, x: int):
    print(s[x-1])


inputNum = list(map(int, input().split()))

N = inputNum[0]
Q = inputNum[1]
s = input()
for i in range(Q):
    inputNum = list(map(int, input().split()))

    func = inputNum[0]
    x = inputNum[1]
    if func == 1:
        s = func_1(s, x)
    else:
        func_2(s, x)
