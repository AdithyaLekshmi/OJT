import pandas as pd
#create a dataframe with a dictionary
data={'name':['kingini','tuttu','ikka'],
      'Age':[24,23,24],
      'Place':['Koovode','mavoor','Punoor']}
df=pd.DataFrame(data)
# print(df)
# print(df[['name','Place']])

# print(df.iloc[2])
# print(df[df['Age']>23])
df['stiphend']=[15000,5000,5000]
df=df.drop(columns=['Age'])
print(df)
print(df.describe())