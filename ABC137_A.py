inputNum = list(map(int, input().split()))

A = inputNum[0]
B = inputNum[1]

plusAnswer = A + B
minusAnswer = A - B
multiAnswer = A * B

maxAnswer = plusAnswer
if (maxAnswer < minusAnswer):
    maxAnswer = minusAnswer
if (maxAnswer < multiAnswer):
    maxAnswer = multiAnswer

print(maxAnswer)
