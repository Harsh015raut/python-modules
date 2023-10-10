import pandas as pd

df = pd.read_csv('survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

#Now we want data of only a specific class,we can use filter for it.
print(df.head())

#Making filter of High salary

# high_salary = (df['ConvertedComp'] > 70000)
# print(df.loc[high_salary,['Country','LanguageWorkedWith','ConvertedComp']])

countries = ['United States','India','United Kingdom','Germany','Canada']
filt = df['Country'].isin(countries)  #is in is used
print(df.loc[filt,'Country'])

filt1 = df['LanguageWorkedWith'].str.contains('Python',na = False)#does it contain python
print(df.loc[filt1,'LanguageWorkedWith'])
