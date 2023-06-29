inFp = None  # 입력 파일
inStr = ""  # 읽어온 문자열
lineCtn = 1

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d : %s" % (lineCtn, inStr), end="")
    lineCtn += 1
inFp.close()
