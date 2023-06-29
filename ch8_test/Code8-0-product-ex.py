import sqlite3

con = sqlite3.connect("productDB")
cur = con.cursor()

cur.execute("CREATE TABLE productTable(pCode char(5), pName char(15), price int, amount int)")

cur.execute("INSERT INTO productTable VALUES('p0001', '상품1', 110, 5)")
cur.execute("INSERT INTO productTable VALUES('p0002', '상품2', 3, 22)")
cur.execute("INSERT INTO productTable VALUES('p0003', '상품3', 2, 11)")

con.commit()