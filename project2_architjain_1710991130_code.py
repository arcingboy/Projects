# -*- coding: utf-8 -*-
"""project2_ArchitJain_1710991130_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cRgz-J03GngPIEahWEnYQrVNhQG24rzI
"""

import numpy as np
import pandas as pd

df1=pd.read_csv('/content/AttendancePercentageWiseReport.csv')
df1

df_temp=df1[4:652]
df_temp=df_temp.reset_index(drop=True)#just reset the index to reorder it correctly
df_temp.head()

#replacing some NaN values with needed column names
df_temp['For Time Table'].head(1).fillna('Serial no.',inplace=True)
df_temp['NVU-Odd Sem'].head(1).fillna('Roll no.',inplace=True)
df_temp['Unnamed: 2'].head(1).fillna('Uni_Id',inplace=True)
df_temp['Unnamed: 3'].head(1).fillna('Student Name',inplace=True)
df_temp['Unnamed: 31'].head(1).fillna('Total %age',inplace=True)
df_temp.head()

df_temp.columns=df_temp.iloc[0]#now assigning that row as columns and then droping the row since it is not needed. 
df_temp=df_temp.drop(df_temp.index[0])
df_temp.head()

df_temp.replace('\xa0---',9999,inplace=True)  #replacing some wanted value with the one which is compatible with our data(x > 100)
df_temp.head()

df_temp.columns=df_temp.columns.str.strip('\xa0')  #removing extra spaces  
df_temp.columns

df_temp=df_temp.astype({'Roll no.' : int , 'Uni_Id' : int ,'AML3201' : float, 'CSL2301' : float , 'CSL3307' : float , 'CSL4207' : float , 'CSL4208' : float , 
                        'CSL4305' : float , 'CSL4318' : float , 'CSL4336' : float , 'CSL5210' : float , 'CSP2301' : float , 'ECL3311' : float , 'GEW1601' : float , 
                        'GEW1603' : float , 'GEW1604' : float , 'GEW1605' : float , 'GEW1607' : float , 'GEW1608' : float , 'GEW1609' : float , 'GEW1610' : float , 
                        'GEW1611' : float , 'GEW1613' : float , 'HUL2401' : float , 'HUL3301' : float , 'AMP1201' : float , 'CSP1307' : float , 'CSP2210' : float , 
                        'ECP1311' : float , 'Total %age':float})
df_temp.dtypes   #converting the data types for the precise results.

df_temp.head()

"""ATTENDANCE OK LIST"""

attend = df_temp[(df_temp['AML3201'] >= 75.00) & (df_temp['CSL2301'] >= 75.00) & (df_temp['CSL3307'] >= 75.00) & (df_temp['CSL4207'] >= 75.00) & (df_temp['CSL4208'] >= 75.00) & (df_temp['CSL4305'] >= 75.00) & (df_temp['CSL4318'] >= 75.00)
            & (df_temp['CSL4336'] >= 75.00) & (df_temp['CSL5210'] >= 75.00) & (df_temp['CSP2301'] >= 75.00) & (df_temp['ECL3311'] >= 75.00) & (df_temp['GEW1601'] >= 75.00) & (df_temp['GEW1603'] >= 75.00) & (df_temp['GEW1604'] >= 75.00) &
            (df_temp['GEW1605'] >= 75.00) & (df_temp['GEW1607'] >= 75.00) & (df_temp['GEW1608'] >= 75.00) & (df_temp['GEW1609'] >= 75.00) & (df_temp['GEW1610'] >= 75.00) & (df_temp['GEW1611'] >= 75.00) & (df_temp['GEW1613'] >= 75.00) & 
            (df_temp['HUL2401'] >= 75.00) & (df_temp['HUL3301'] >= 75.00) & (df_temp['AMP1201'] >= 75.00) & (df_temp['CSP1307'] >= 75.00) & (df_temp['CSP2210'] >= 75.00) & (df_temp['ECP1311'] >= 75.00)]
attend.replace(9999.00,'---',inplace=True)
attend.head()
#attend.to_csv('Attendance_ok.csv')

"""# MAKE UP LIST

STUDENTS WHO ARE HAVING LESS THAN 75% ATTENDANCE IN ANY ONE SUBJECT

IN PRACTICAL
"""

practical=df_temp.iloc[0:,[0,1,2,3,27,28,29,30,31]]
practical = practical[(practical['AMP1201'] < 75.00) | (practical['CSP1307'] < 75.00) | (practical['CSP2210'] < 75.00) | (practical['ECP1311'] < 75.00)]
practical.replace(9999.00,'---',inplace=True)
practical.head()
#practical.to_csv('Practical_Make_up_list.csv')

"""IN THEORY"""

#Theory=pd.merge(df_temp.iloc[0:,0:26], df_temp.iloc[0:,31], how='outer', left_index=True, right_index=True)
for i in df_temp.columns[4:31]:
  Theory=df_temp[df_temp[i]<75.00]
Theory.replace(9999.00,'---',inplace=True)
Theory.head()
#Theory.to_csv('Theory_make_up_list.csv')

