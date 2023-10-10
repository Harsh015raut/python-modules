import pandas as pd
people = {
    'first' : ['harsh','arpita','ajinkya'],
    'last' : ['raut','pol','temgire'],
    'email' : ['hsr015@gmail.com','app05@gmail.com','ajr21@gmail.com']
}
df = pd.DataFrame(people)

#Combining first and last name column and making a new column
df['full_name'] = (df['first'] + ' ' + df['last'])
print(df)   

df.drop(columns =['first','last'],inplace = True)
print(df)

df[['first','last']] = df['full_name'].str.split(' ',expand = True)
#expands the splitted columns
print(df)


#Adding a single row
#df.append({'first':'tony'},ignore_index = True)
#print(df)
people1 = {
    'first' : ['iron','captain'],
    'last' : ['man','america']
   
}
df2 = pd.DataFrame(people1)
df = df._append(df2,ignore_index = True,sort = False)
print(df)

# dropping
filt = df['last'] == 'temgire'
df.drop(index = df[filt].index,inplace=True )
print(df)

