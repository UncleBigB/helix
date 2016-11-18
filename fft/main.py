import pandas as pd
import numpy as np
import MySQLdb
from matplotlib import pyplot as plt

# 从数据库中取出数据
symbol = "sh000001"
conn = MySQLdb.connect(host='localhost', user='root', db='stock')
df = pd.read_sql(
    "SELECT * FROM stockdaykline WHERE symbol = '%s' AND date >= '2016-01-01'" %
    (symbol),
    con=conn,
    index_col=['date'],
    parse_dates=['date'])
ts = df.close

f = np.fft.fft(ts)
fshift = np.fft.fftshift(f)
fimg = np.log(np.abs(fshift))

plt.figure()
plt.grid(True)

#收盘价趋势
plt.subplot(2, 1, 1)
plt.title("上证指数")
plt.plot(ts.index, ts.values)

#傅里叶变换
plt.subplot(2, 1, 2)
plt.title("FFT")
plt.plot(fimg)

plt.show()
