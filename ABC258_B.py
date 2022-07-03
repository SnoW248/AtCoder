inputNum = int(input())

df = []
for i in range(inputNum):
    l = [x for x in list(str(input()))]
    df.append(l)

ans=0
for i in range(inputNum):
  for j in range(inputNum):
    for dx in [-1,0,1]:
      for dy in [-1,0,1]:
        if dx==0 and dy==0:
          continue
        a=int("".join([df[(i+dx*r)%inputNum][(j+dy*r)%inputNum] for r in range(inputNum)]))
        ans=max(a,ans)
print(ans)