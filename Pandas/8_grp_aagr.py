import pandas as pd

df = pd.read_csv('survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

#Aggregations - Combining multiple pieces of data to give single output
#aggregators are mean,median,mode
print(df['ConvertedComp'].median())

#If we want to take median for entire df
# print(df.median())

print(df.describe()) #It gives us count,mean,std,25 percentile,75percentile n all
print("Total entries for salary is:",df['ConvertedComp'].count()) #Used to count valid count

#In Hobbyist we want to know how many people said yes and how m any said no
print("Answer of Hobbyist is:",df['Hobbyist'].value_counts())

#
print(schema_df.loc['SocialMedia'])
print(df['SocialMedia'].value_counts())
#Now if we want this data in percentage form,then we pass normalise=True
print(df['SocialMedia'].value_counts(normalize=True))

#Group-By Operations - involves sliiting the object,applying function and combining results

print(df['Country'].value_counts())

#Here we have grouped our rows by country
country_grp = df.groupby(['Country'])

#Here we get al data of people who are from US
print(country_grp.get_group('United States'))

#Here we get al data of people who are from India
print(country_grp.get_group('India'))
#This is similar to a filter.
'''
filt = df['Country'] == ['United States']
df.loc[filt]
'''
#Due to group by,we can use it for multiple countries

#Most popular social mediain India
print(country_grp['SocialMedia'].value_counts().loc['India'])

#Median Salaries of all countries
print(country_grp['ConvertedComp'].median())

#NOw we want to use multiple aggregators,we use .agg and pass a list of agg functions
print(country_grp['ConvertedComp'].agg(['mean','median']))

#For specific country
print(country_grp['ConvertedComp'].agg(['mean','median']).loc['India'])

#How many people in India have expertise in Python
# filt = df['Country'] == 'India'
# p = df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()
# print("Number of people who have expertise in python in India are(filter method):",p)

#Same Question with group by

p = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
print("Number of people who have expertise in python are(groupby apply method)",p)

country_respondents = df['Country'].value_counts()
print(country_respondents)

py_df = pd.concat([country_respondents,p],axis = 'columns',sort = False)
#print(py_df)

#Renaming columns
py_df.rename(columns={'count':'NumRespondents','LanguageWorkedWith':'NumknowsPython'},inplace=True)
print(py_df)

#Adding pct column

py_df['PctKnowsPython'] = (py_df['NumknowsPython']/py_df['NumRespondents'])* 100
print(py_df)

py_df.sort_values(by='PctKnowsPython',ascending = False,inplace = True)
print(py_df.head(50))
print(py_df.loc['Japan'])








