import pandas as pd
import numpy as nd
import MySQLdb
import matplotlib.pyplot as plt

#从数据库中取出数据
conn = MySQLdb.connect(host='localhost', user='root', db='stock')
symbol = "sh601919"
df = pd.read_sql("select * from stockdaykline where symbol = '%s'" % symbol, con=conn, index_col=['date'])

#生成时间序列
ts = pd.Series(df['open'], index=df.index)
ts = ts[ts.values > 0][-200:]

#绘图
plt.figure()
ts.plot(title=df['name'][-1], grid=True)
plt.show()



