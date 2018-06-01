# from pandas import Series, DataFrame
# import pandas as pd
#
# data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
#
# df = DataFrame(data, index=list(range(1, 6)),
#                columns=['year', 'state', 'pop', 'name'])
# print(df)
# #
# # print('\n', '---------------')
# print(list(df.ix[3]))
# #
# # print('\n', '---------------')
# print(list(df['year']))
#
# aList = ['']
# bList = ['aa', 'bb', 'cb', 'dd']
# cList = ['lemon', 'apple', 'orange', 'banana']
# #
# d = {'num': aList, 'char': bList, 'fruit': cList}
# #
# df1 = DataFrame(d, index=['a', 'b', 'c', 'd'])
# # df2 = DataFrame(bList)
# print('\n', '---------------')
# print(df1)
# # print(df1.num)
# #
# # print('\n', '---------------')
# # print(df1.ix['b'])  # 获取索引号为 'b' 的行的数据
# #
# print('\n', '---------------')
# # print(df1.ix[:2, 1:3])  # 以切片形式获取部分数据
# # df.to_csv('b.csv', index=False, sep=',')
#
# data = pd.read_csv('b.csv')
# print(data.sum(axis=1))
#
# # import pandas as pd
# #
# # a = ['one', 'two', 'three']
# # b = [1, 2, 3]
# # english_column = pd.Series(a, name='english')
# # number_column = pd.Series(b, name='number')
# # predictions = pd.concat([english_column, number_column], axis=1)
# # # another way to handle
# # save = pd.DataFrame({'english': a, 'number': b})
# # save.to_csv('b.csv', index=False, sep=',')

import ahocorasick

A = ahocorasick.Automaton()

# 向trie树中添加单词
for index, word in enumerate("he her hers she".split()):
    A.add_word(word, (index, word))
# 用法分析add_word(word,[value]) => bool
# 根据Automaton构造函数的参数store设置，value这样考虑：
# 1. 如果store设置为STORE_LENGTH，不能传递value，默认保存len(word)
# 2. 如果store设置为STORE_INTS，value可选，但必须是int类型，默认是len(automaton)
# 3. 如果store设置为STORE_ANY，value必须写，可以是任意类型

# 测试单词是否在树中
if "he" in A:
    print(True)
else:
    print(False)
A.get("he")
# (0,'he')
A.get("cat", "<not exists>")
# '<not exists>'
# A.get("dog")
# # KeyError

# 将trie树转化为Aho-Corasick自动机
A.make_automaton()

# 找到所有匹配字符串
for item in A.iter("_hershe_"):
    print(item)
# (2,(0,'he'))
# (3,(1,'her'))
# (4, (2, 'hers'))
# (6, (3, 'she'))
# (6, (0, 'he'))


import pandas as pd
import pymysql
import sys
from sqlalchemy import create_engine


def read_mysql_and_insert(id, question, answer):
    # try:
    #     conn = pymysql.connect(host='localhost', user='root', password='Admin@123', db='test', charset='utf8')
    # except pymysql.err.OperationalError as e:
    #     print('Error is ' + str(e))
    #     sys.exit()

    # cur = conn.cursor()
    sql = 'INSERT INTO data_admin_question_auto (id, question, answer, agrees) VALUES ("{}","{}","{}", 0);'.format(id, question, answer)
    # cur.execute(sql)
    # conn.commit()
    print('@@@@@@@@@@@')
    return sql


class MysqlConn(object):
    def __init__(self):
        self.db = pymysql.connect(host='139.199.23.193', user='hemei',
                                  password='Hemei@123',
                                  db='intelligentcs',
                                  port=3306, charset='utf8')
        self.cur = self.db.cursor()

    def execute(self, exec_sql):
        self.cur.execute(exec_sql)
        return self.cur.fetchall()

    def commit(self):
        self.db.commit()


if __name__ == '__main__':
    try:
        conn = MysqlConn()
    except pymysql.err.OperationalError as e:
        print('Error is ' + str(e))
        sys.exit()
    my_sql = 'select MAX(id) from data_admin_question_auto ORDER BY id DESC ;'
    id_cur = conn.execute(my_sql)
    q_id = id_cur[0][0]
    df = pd.read_excel(r'智能交互平台场景及测试用例.xlsx', sheet_name='系统画像')
    sql = ''

    for k, v in df.iterrows():
        print('##################')
        q_list = v['问题'].split('\n')
        a_list = v['答案'].split('\n')
        q_n = len(q_list)
        a_n = len(a_list)
        for n, q in enumerate(q_list):
            if q_id:
                q_id += 1
            else:
                q_id = 1
            question = q
            if n < min(q_n, a_n):
                answer = a_list[n]
            else:
                answer = a_list[q_n % a_n]
            print(read_mysql_and_insert(q_id, question, answer))
            conn.execute(read_mysql_and_insert(q_id, question, answer))
    conn.commit()
