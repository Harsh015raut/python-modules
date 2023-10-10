import pandas as pd
import numpy as np

na_vals = ['NA','Missing']
df = pd.read_csv('survey_results_public.csv',index_col='Respondent',na_values=na_vals)
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

#Calculate the avg coding exp in years.
print(df['YearsCode'].head(10))

#For taking all unique values of Columns,we run the following code
print(df['YearsCode'].unique())
#Results:
# ['4' nan '3' '16' '13' '6' '8' '12' '2' '5' '17' '10' '14' '35' '7'
#  'Less than 1 year' '30' '9' '26' '40' '19' '15' '20' '28' '25' '1' '22'
#  '11' '33' '50' '41' '18' '34' '24' '23' '42' '27' '21' '36' '32' '39'
#  '38' '31' '37' 'More than 50 years' '29' '44' '45' '48' '46' '43' '47'
#  '49']
df['YearsCode'].replace('Less than 1 year',0,inplace=True)
df['YearsCode'].replace('More than 50 years',51,inplace=True)
print(df['YearsCode'].unique())
#Converting string into float
df['YearsCode'] = df['YearsCode'].astype(float)
# print("The avg years for developers who accessed this surveys is:",df['YearsCode'].mean())
print("The avg years for developers who accessed this surveys is:",df['YearsCode'].median())
df['YearsCode']




