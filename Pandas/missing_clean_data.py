import pandas as pd
import numpy as np
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df = pd.DataFrame(people)
pd.set_option('display.max_columns',4)
print(df)
print("\n")
df.dropna(axis = 'index',how = 'any') #Default Mode
#Results: 
#        first     last                    email      age
# 0  Corey  Schafer  CoreyMSchafer@gmail.com       33
# 1   Jane      Doe        JaneDoe@email.com       55
# 2   John      Doe        JohnDoe@email.com       63
# 6     NA  Missing                       NA  Missing
print(df)
df.dropna(axis = 'index',how = 'all') #all signifies that we will drop the row where all values are missing.
#Results:
#    first     last                    email      age
# 0  Corey  Schafer  CoreyMSchafer@gmail.com       33
# 1   Jane      Doe        JaneDoe@email.com       55
# 2   John      Doe        JohnDoe@email.com       63
# 3  Chris  Schafer                     None       36
# 5   None      NaN      Anonymous@email.com     None
# 6     NA  Missing                       NA  Missing
# print(df)
df.dropna(axis = 'columns',how = 'all') #Since columns donot have all Nan,hence whole table will be return.
print(df)
#Results:
#    first     last                    email      age
# 0  Corey  Schafer  CoreyMSchafer@gmail.com       33
# 1   Jane      Doe        JaneDoe@email.com       55
# 2   John      Doe        JohnDoe@email.com       63
# 3  Chris  Schafer                     None       36
# 4    NaN      NaN                      NaN     None
# 5   None      NaN      Anonymous@email.com     None
# 6     NA  Missing                       NA  Missing

df.dropna(axis = 'index',how = 'all',subset = ['email'])#,inplace = True)
print(df)
#Results:
#    first     last                    email      age
# 0  Corey  Schafer  CoreyMSchafer@gmail.com       33
# 1   Jane      Doe        JaneDoe@email.com       55
# 2   John      Doe        JohnDoe@email.com       63
# 5   None      NaN      Anonymous@email.com     None
# 6     NA  Missing                       NA  Missing

df.replace('NA',np.nan,inplace=True)      #Na replaced with NaN
df.replace('Missing',np.nan,inplace=True) #Missing replcaed with NaN
print(df)
#Results:
#    first     last                    email   age
# 0  Corey  Schafer  CoreyMSchafer@gmail.com    33
# 1   Jane      Doe        JaneDoe@email.com    55
# 2   John      Doe        JohnDoe@email.com    63
# 3  Chris  Schafer                     None    36
# 4    NaN      NaN                      NaN  None
# 5   None      NaN      Anonymous@email.com  None
# 6    NaN      NaN                      NaN   NaN

#df.fillna() -> replaces missing value of Program
print(df.dtypes)  #gives data types of each column

#Since our age data is stored as string,we need to type cast it into float.we convert to float as NaN value is by default a float,if we set int,error might occur.
df['age'] = df['age'].astype(float) #astype() is used for type casting
print(df.dtypes)
print(df['age'].mean())



