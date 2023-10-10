# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:46:42 2023

@author: Harsh
"""

import pandas as pd
people = {
    'first' : ['harsh','arpita','ajinkya'],
    'last' : ['raut','pol','temgire'],
    'email' : ['hsr015@gmail.com','app05@gmail.com','ajr21@gmail.com']
}
df = pd.DataFrame(people)
df.sort_values(by = ['last','first'],ascending=False,inplace=True)

#By default ascending is set to zero
print(df)

df.sort_values(by = ['last','first'],ascending=[False,True],inplace=True)
print(df)



