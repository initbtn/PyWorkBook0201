import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

## 메인 코드 부분 ##
con = sqlite3.connect("productDB")
cur = con.cursor()

cur.execute("SELECT * FROM productTable")

print("상품코드    상품이름    가격    수량")
print("--------------------------------------------------------")

while (True) :
    row = cur.fetchone()
    if row == None :
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %5d   %5d" % (data1, data2, data3, data4))

con.close()
