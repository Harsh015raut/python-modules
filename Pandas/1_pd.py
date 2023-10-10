import pandas as pd
#Loading Data
df = pd.read_csv('survey_results_public.csv') #Loading CSV Data
schema_df = pd.read_csv('survey_results_schema.csv')
# print(df)
print(df.shape)  #Gives shape of Data .shape is Attribute
print(df.info()) #.info is a method and hence it requires parenthesis().
#info methods gives us information of all our data.

#Lets see all the Columns
pd.set_option('display.max_columns',85) #Will let us see all the columns
pd.set_option('display.max_rows',85) #Will display all rows


print(schema_df)
print(df.head(10)) #This shows us first 10 rows)
print(df.tail(10)) #This shows us last 10 rows)

print(df.shape)

#Let see all columns available
print(df.columns)
print(df['Hobbyist'])
print(df['Hobbyist'].value_counts()) #Counts no's and yes

#For grabbing rows,we will use loc as it allows us giving labels
print(df.loc[[0,1,2],'Hobbyist'])

#For using slicing,we donot need to wrap values in square brackets
print(df.loc[0:2,'Hobbyist'])
#For getting all the columns from Hobbyist to Employment,we use slicing
print(df.loc[0:2,'Hobbyist':'Employment']) #Only difference is that slicing in DataFrame is inclusive of both

#Lets Change Index of Data to respondent as we already have unique value available
df = pd.read_csv('survey_results_public.csv',index_col='Respondent')

print(schema_df)
schema_df = pd.read_csv('survey_results_schema.csv',index_col='Column')
print(schema_df.loc['MgrIdiot','QuestionText'])
#For sorting indexes
schema_df.sort_index() #inplcae = true changes original DF