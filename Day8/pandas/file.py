import pandas as pd
df=pd.read_csv('detail.csv',
               dtype={'Age':float,'Name':str},
               
               usecols=['Name','Age','Place'])
print(df)