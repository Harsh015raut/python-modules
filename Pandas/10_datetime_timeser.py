import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

d_parser = lambda x: pd.to_datetime.strptime(x,'%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv',parse_dates= ['Date'],date_parser = d_parser)
print(df.head())
print(df.shape)
print(df.loc[0,'Date'])

#Converting column to a date time
# df['Date'] = pd.to_datetime(df['Date'],format = '%Y-%m-%d %I-%p')
print(df['Date'])

