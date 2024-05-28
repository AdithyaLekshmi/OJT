import pandas as pd
#series: which is 1D
data=[10,2,3,45,65,2]
series=pd.Series(data)
print(series)

#access the element seperately by using indexing
print(series[0])

#arithmetic operation
series_add=series+10
print(series_add)

#filter the value which is grater than 20 in the series.
print(series[series>20])
#statistical method

mean=series.mean()
print(f"The mean of the series is:{mean}")
median=series.median()
print(f"The median of the series is:{median}")
mode=series.mode()
print("The mode of the series is:",mode)