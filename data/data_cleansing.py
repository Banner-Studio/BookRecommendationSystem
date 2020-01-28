import pandas as pd
import re
# 进行数据清洗，将需要的数据导入到数据库中

dataReaded = pd.read_excel('2016-2018借书.xlsx')
# print(dataReaded[:5])
# print(dataReaded.columns)
# Index(['序号', '馆藏号', '馆藏', '索书号', '题名', '读者', '读者号', '借书操作员', '借书日期', '还书操作员',
#        '还书日期'],
rdataReaded = dataReaded[['读者号', '读者']].drop_duplicates(['读者号', '读者'])
print(rdataReaded[:5])
# pd.Series(['1', '2', '3a', '3b', '03c']).str.match(pattern)
# data.column.str.extract(r'((\d\s)??\d3?[-\s]\d{3}[-\s]\d{4})')
pattern = r'(2\d{10})'
# pattern = r'(.*)'
# rdataReaded['读者号'] = rdataReaded['读者号'].str.extract(pattern)
# print(rdataReaded[:5])
#
r = rdataReaded['读者号'].tolist()
p = []
for i in r[:5]:
    r = re.findall(pattern, str(i))
    if len(r) > 0:
        print(r)
        p.append(r)
# df[[(len(x) < 2) for x in df['column name']]]
# df = df.drop(df[df.score < 50].index)
rdataReaded = rdataReaded.drop(rdataReaded['读者号' not in p].index)
print(rdataReaded[:5])



