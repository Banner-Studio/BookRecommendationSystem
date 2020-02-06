import sys
import pandas as pd
import re
import time
import threading
# 进行数据清洗，将需要的数据导入到数据库中

dataReaded = pd.read_excel('2016-2018借书.xlsx')


def clean(df, pattern=r'(2\d{10})'):
    """筛选出可利用的数据"""
    r = df.tolist()
    p = []
    for i in r:
        r = re.findall(pattern, str(i))
        if len(r) > 0:
            # print(r)
            p.append(int(r[0]))
    return p


# 去重
rdataReaded = dataReaded[['读者号', '读者']].drop_duplicates(['读者号', '读者'])
# 清洗数据
rdataReaded = rdataReaded.where(rdataReaded['读者号'].isin(clean(rdataReaded['读者号'])))
rdataReaded = rdataReaded.dropna(axis=0)
print('开始存数据1')
# 存数据到excel表格中
rdataReaded.to_excel('rdataReaded.xlsx', index=False, sheet_name='rdataReaded')


bdataReaded = dataReaded[['题名', '馆藏', '读者号']]
bdataReaded = bdataReaded.where(bdataReaded['读者号'].isin(clean(bdataReaded['读者号'])))
bdataReaded = bdataReaded.dropna(axis=0)
print('开始存数据2')
# 存数据到excel表格中
bdataReaded.to_excel('bdataReaded.xlsx', index=False, sheet_name='bdataReaded')

# 读取数据
data_readerinfo = pd.read_excel('data_readerinfo.xlsx')
bdataReaded['读者号id'] = 0
it1 = iter(range(bdataReaded.shape[0]))
start = time.clock()


class GetIdThread(threading.Thread):
    """单线程"""
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('开始线程')
        get_id_main()
        print('退出线程')


def get_id_main():
    """根据另一个表中的数据，修改本表的数据"""
    while True:
        try:
            r1 = next(it1)
            it2 = iter(range(data_readerinfo.shape[0]))
            for r2 in it2:
                if bdataReaded.iloc[r1, 2] == data_readerinfo.iloc[r2, 1]:
                    bdataReaded.iloc[r1, 3] = data_readerinfo.iloc[r2, 0]
                    print(bdataReaded.iloc[r1, 3])
                    break

        except StopIteration:
            print('用时：', time.clock() - start)
            bdata_readed = bdataReaded.drop_duplicates(subset=['题名', '读者号id'])
            bdata_readed.to_excel('bdataReaded.xlsx', index=False, sheet_name='new_bdataReaded')
            sys.exit()


thread = GetIdThread()
thread.start()
thread.join()
print('退出主线程')
