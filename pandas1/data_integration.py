#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

import pandas as pd
from pandas import Series,DataFrame

'''
将三个表格合为一张合理的表
'''

# 美国各州面积
areas = pd.read_csv('./state-areas.csv')
# print(areas.shape)
# (52,2)

# 美国各州缩写
abb = pd.read_csv('./state-abbrevs.csv')
# print(abb.shape)
# (51,2)

# 美国各州人口
pop = pd.read_csv('./state-population.csv')
# print(pop.shape)
# (2544,4)


pop2 = pop.merge(abb,how = 'outer',
                 left_on='state/region',
                 right_on='abbreviation')
# print(pop2.shape)
# (2544,6)

# 级联后数据变少了96个
print(pop2.isnull().any())
print(pop2.head())
pop2.drop(labels='abbreviation',
          axis=1,
          inplace=True)
print(pop2.isnull().any())


# 定位空数据
cond = pop2['state'].isnull()
# print(cond)

# 去重
pop2[cond]['state/region'].unique()
# array(['PR', 'USA'], dtype=object)


cond = pop2['state/region'] == 'PR'
# print(cond)
pop2['state'][cond]='Puerto Rico'
cond = pop2['state/region'] == 'USA'
pop2['state'][cond] = 'United State'
# print(pop2.isnull().any())
cond = pop2['population'].isnull()
# pop2[cond].shape
# pop2.shape
pop2.dropna(inplace=True)
# pop2.isnull().any()


pop3 = pop2.merge(areas, how='outer')
# pop3.isnull().any()
cond1 = pop3['area (sq. mi)'].isnull()
# print(pop3[cond1])
a = areas['area (sq. mi)'].sum()
# print(a)
cond2 = pop3['state'] == "United State"
pop3['area (sq. mi)'][cond2] = a
# print(pop3.notnull().all())


pop_density = (pop3['population']/pop3['area (sq. mi)']).round(1)
pop_density = DataFrame(pop_density)
pop_density.columns = ['pop_density']
# print(pop_density.head())

pop4 = pop3.merge(pop_density, left_index=True, right_index=True)
pop4['year'].unique()
pop4['ages'].unique()
pop5 = pop4.query("year == 2012 and ages == 'total'")
pop5.set_index(keys='state/region', inplace=True)

print(pop5.sort_values(by='pop_density'))

print(pop5.sort_values(by='pop_density', ascending=False))
