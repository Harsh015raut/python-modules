import pandas as pd
people = {
    'first' : ['harsh','arpita','ajinkya'],
    'last' : ['raut','pol','temgire'],
    'email' : ['hsr015@gmail.com','app05@gmail.com','ajr21@gmail.com']
}
df = pd.DataFrame(people)
print(df)

# print(type(df['email'])) 

# #Accessing a Single column
# print(df['email'])  #This is a better method #Gives series.
# print(df.email)     #If the method name and column name is same,then method will execute,henc it it is not used widely 

# #For accessing Multiple Columns
# print(df[['last','email']]) #DataFrame is generated

# #For getting names of Columns,we use df.columns
# print(df.columns)

# #iloc - allows us to access rows the by integer location
# print(df.iloc[0])  #Returns 1st row of data.

# #for selecting multiple lists,we pass a list of index
# print(df.iloc[[1,2]])

# #for columns 
# print(df.iloc[[1,2],1]) #Will return Only column with index 1 for entries.

# print(df)
# print(df.loc[0]) #Works similar to iloc
# #loc-we can use labels in loc function whereas in iloc we need integer
# print(df.loc[[0,1],['email','first']])

# #Setting Custom Index
# #Set email addresses as indexes for df
# print(df.set_index('email')) #This does not change the DataFrame,it just shows us a changed view

# #Now if we really want to make changes in DataFrame and change index to emailmthen we use inplcae = True
# print(df.set_index('email',inplace = True))
# print(df)

# print(df.index) #Prints Index of Df

# #Reset index - used to reset index to original
# print(df.reset_index(inplace = True))

# #Filter
# filt = (df['last'] == 'raut') #returns series of true/false values
# print(df[filt]) #Returns DF of last == raut

# print(df.loc[filt,'email'])

# filt = ((df['last'] == 'raut') & (df['first'] == 'harsh')) 
# print(df.loc[filt,'email'])

# #Filter negation
# print(df.loc[~filt,'email']) #Will return all values without raut and harsh

print(df.columns)
 #Changing column names
df.columns = ['first_name','last_name','email']
print(df)
 #For lowercasing the columns,reducing spaces

df.columns = [x.upper() for x in df.columns]
print(df)

#Editing column by making them str and doing operations
df.columns = df.columns.str.replace('_',' ')
print(df)
 #renaming columns
df.rename(columns={'FIRST NAME':'first','LAST NAME':'last'},inplace=True)
print(df)

#Changing value in a row using iloc
# print(df.loc[2])
print(df.loc[2,['last','EMAIL']])
#.at can also be used instead of .loc

# print(df.at[2,'last'] = 'T')
df['EMAIL'] = df['EMAIL'].apply(lambda x:x.upper())
print(df)

#apply is used on series objects of a df.

print(df.apply(pd.Series.min))  #Print ajr as in sorted,a comes first

#For appyling a function to every indivisual element in the element.
#we use applymap
print(df.applymap(len))  #Gives lenght of each element
df.applymap(str.lower)
print(df)

#map methods - used for substitution

# print(df['first'].map({'harsh':'HR','arpita':'AP'}))

#Values which we did not substitute get converted to NaN value.

#We will use replace to change only few name
df['first'] = df['first'].replace({'harsh':'HR','arpita':'AP'})
print(df)

#

