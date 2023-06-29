import sqlite3

con = sqlite3.connect("productDB")
cur = con.cursor()

while True:
    data1 = input("상품코드 ==> ")
    if data1 == "":
        break
    data2 = input("상품이름 ==> ")
    data3 = input("가격 ==> ")
    data4 = input("수량 ==> ")
    sql = (
        "INSERT INTO productTable VALUES('"
        + data1
        + "','"
        + data2
        + "',"
        + data3
        + ","
        + data4
        + ")"
    )
    cur.execute(sql)

con.commit()
con.close()
