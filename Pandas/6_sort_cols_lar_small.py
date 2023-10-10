import pandas as pd

df = pd.read_csv('survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
print(df)
df.sort_values(by = ['Country','ConvertedComp'],ascending = [True,False],inplace = True)
df['Country'].head(50)
print(df[['Country','ConvertedComp']].head(50))


#nlargest() Method
print(df['ConvertedComp'].nlargest(10)) #10 signifies top 10 values
#

#IF we want to see other data of these rows,then we apply this to whole dataframe
df = df.nlargest(10,'ConvertedComp')
#This sorts the whole data according to columns and shows all other attributes of data.
print(df)

