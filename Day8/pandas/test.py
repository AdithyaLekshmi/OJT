import pandas as pd
df=pd.read_csv('detail.csv')
# print(df)

df_cleaned=df.dropna(how='all')
print(df_cleaned)