# -*- coding: utf-8 -*-
"""KDD

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kaiW-i47NtglE7eRTGZ86b8El0HnxOL6
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = '/content/KDDTest-21.txt'

df = pd.read_csv(data)
#Shapes of datasets:
print('shape of KDD dataset(Rows, Columns):',df.shape)

print(df.head())



columns = (['duration'
,'protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations','num_shells','num_access_files'
,'num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate'
,'dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','attack','level'])

df.columns = columns

# sanity check
df.head()

#continuous Data
print("continuous/Numeric")
print(df._get_numeric_data().columns,"\n")

#Categorical Data
print("Categorical")
for i in df:
  if(df[i].dtype==object):
     print(df[i].name,df[df[i].name].unique(),'\n')

#Shapes of datasets:
print('shape of KDD dataset(Rows, Columns):',df.shape)

#check for missing and null value in a column

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
print('\n')
print('Count NUll values : ')
typ=df.dtypes
print(typ)

"""Scatter"""

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = df['level'], y = df['protocol_type'])
plt.xlabel("level")
plt.ylabel("protocol_type")
plt.show()

df.plot.scatter(y='service', x='level')

df.plot.scatter(y='flag', x='level')

"""LINE """

# ax = df_monthly_discount.plot.line(x = 'InvoiceMonth', y = 'TransactionDiscount', color = 'lime')
df1=df[:1000]
df1.plot.line(x = 'duration', y = 'level')