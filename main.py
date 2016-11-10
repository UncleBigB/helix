import pandas as pd
import numpy as np
import MySQLdb
import matplotlib.pyplot as plt

#从数据库中取出数据
conn = MySQLdb.connect(host='localhost', user='root', db='stock')
symbol = "sh600123"
df = pd.read_sql("select * from stockdaykline where symbol = '%s'" % symbol, con=conn, index_col=['date'], parse_dates=['date'])
ts = df.close

#计算与绘图
plt.figure()
ts = ts['2015':'2016']
ts.plot(title=df['name'][-1], grid=True)

ts = ts.rolling(window=12, center=False).mean()
ts.plot(title=df['name'][-1], grid=True)
plt.show()



