import demjson
import urllib.request
import re
import MySQLdb
import time

def fetchStockList():
    resp = urllib.request.urlopen("http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=0&num=8000&sort=symbol&asc=1&node=hs_a")

    data = resp.read().decode('gbk')
    pattern = re.compile(r'\{[^}]+\}')
    stocklist = pattern.findall(data)

    db = MySQLdb.connect(host="localhost", user="root", db="stock")


    for x in stocklist:
        json = demjson.decode(x)
        cur = db.cursor()
        cur.execute("""REPLACE INTO stocklists (symbol, code, name, type) VALUES (%s, %s, %s, '')""", (json['symbol'], json['code'], json['name']))

    db.commit()


def fetchDayKline():
    today = time.strftime("%Y%m%d")
    db = MySQLdb.connect(host="localhost", user="root", db="stock")
    cur = db.cursor()
    cur.execute("SELECT * FROM stocklists")
    l = cur.fetchall()
    for s in l:
        url = "http://quotes.money.163.com/service/chddata.html?code="
        if s[0].startswith("sz"):
            url = url + "1" + s[1]
        elif s[0].startswith("sh"):
            url = url + "0" + s[1]
        else:
            pass

        url = url + "&start=" + today

        print(url)
        resp = urllib.request.urlopen(url)
        data = resp.read().decode('gbk')
        lines = data.split('\r\n')
        for l in lines[1:]:
            l = l.replace("None", "0")
            c = l.split(",")
            if len(c) == 16:
                cur.execute("REPLACE INTO stockdaykline (date, symbol, name, close, high, low, open, yestclose, updatevol, updatepercent, turnoverrate, volume, turnover, marketcap, circulation, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13], c[14], c[15]))
        db.commit()

    cur.execute("UPDATE stockdaykline SET symbol = TRIM(LEADING \"'\" FROM symbol)")
    db.commit()








