import pandas as pd

inputNum = int(input())

df_buf = []
for i in range(inputNum):
    l = [int(x) for x in list(str(input()))]
    print(l, df_buf)
    df_buf.append(l)
df = pd.DataFrame(df_buf)

print(df)

print(df.max().index)