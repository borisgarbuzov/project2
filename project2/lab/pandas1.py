import pandas as pd

# print (pd.__doc__)
print (pd.__package__)
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d);

d2 = {'col1': [1, 2, 3], 'col2': [3, 4]}
# df2 = pd.DataFrame(data=d2);
# why exited with code 0?

import numpy as np
df = pd.DataFrame(data=d, dtype=np.int8)
df.dtypes

df2 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
                   
print(df2)                   
print(df2.T)
print(df2.at)
print(df2.attrs)
print(df2.axes)
#df2[1,1]
print("columns =", df2.columns)
print("columns =", list(df2.columns))
# print("df2.iat(1) =", df2.iat(1))
print(df2.loc[1])
print(df2.loc[1].at['a'])
print(df2.loc[1].at["a"])
df.iloc[[0]]
type(df.iloc[[0]])
df.iloc[[0, 1]]
df.iloc[:3]



 

