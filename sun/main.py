import pandas as pd
import numpy as np
import MySQLdb
import csv

# 从数据库中取出数据
conn = MySQLdb.connect(host='localhost', user='root', db='stock')
cur = conn.cursor()
cur.execute("SELECT symbol,name FROM stocklists ORDER BY symbol")

symbols = cur.fetchall()


result = pd.DataFrame(columns=("symbol", "name", "mean", "std", "cov"))
for s in symbols:
    symbol = s[0]
    name = s[1]
    df = pd.read_sql(
        "SELECT date, close FROM stockdaykline WHERE symbol = '%s' AND date >= '2016-01-01'" %
        (symbol),
        con=conn,
        index_col=['date'],
        parse_dates=['date'])
    ts = df.close
    mean = ts.mean()
    std = ts.std()
    if mean != 0:
        cov = std/mean
    else:
        cov = 0
    result = result.append(pd.DataFrame(
        {"symbol": symbol, "name": name, "mean": mean, "std": std, "cov": cov}, index=[symbol]))

    # print("%s<%s>:%s, %s" % (symbol, name, mean, std))
    print("%s<%s>" % (symbol, name))

result.sort_values(by="cov", ascending=True).to_csv('./result.csv', encoding="gb18030", quoting=csv.QUOTE_ALL, escapechar="\"")
