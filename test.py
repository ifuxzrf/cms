from pandas import Series, DataFrame
import pandas as pd

data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = DataFrame(data, index=list(range(1, 6)),
               columns=['year', 'state', 'pop', 'name'])
print(df)
#
# print('\n', '---------------')
print(list(df.ix[3]))
#
# print('\n', '---------------')
print(list(df['year']))

aList = ['']
bList = ['aa', 'bb', 'cb', 'dd']
cList = ['lemon', 'apple', 'orange', 'banana']
#
d = {'num': aList, 'char': bList, 'fruit': cList}
#
df1 = DataFrame(d, index=['a', 'b', 'c', 'd'])
# df2 = DataFrame(bList)
print('\n', '---------------')
print(df1)
# print(df1.num)
#
# print('\n', '---------------')
# print(df1.ix['b'])  # 获取索引号为 'b' 的行的数据
#
print('\n', '---------------')
# print(df1.ix[:2, 1:3])  # 以切片形式获取部分数据
# df.to_csv('b.csv', index=False, sep=',')

data = pd.read_csv('b.csv')
print(data.sum(axis=1))

# import pandas as pd
#
# a = ['one', 'two', 'three']
# b = [1, 2, 3]
# english_column = pd.Series(a, name='english')
# number_column = pd.Series(b, name='number')
# predictions = pd.concat([english_column, number_column], axis=1)
# # another way to handle
# save = pd.DataFrame({'english': a, 'number': b})
# save.to_csv('b.csv', index=False, sep=',')
