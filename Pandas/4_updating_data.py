import pandas as pd

df = pd.read_csv('survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
df.rename(columns={'ConvertedComp':'SalaryUSD'},inplace= True)
# print(df.columns)
print(df['Hobbyist'])
df['Hobbyist'].map({'Yes':True,'No':False}) #We don't have inplace for map,so we define it in colun
df['Hobbyist'] = (df['Hobbyist'].map({'Yes':True,'No':False}))
print(df['Hobbyist'])