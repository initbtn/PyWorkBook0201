import requests
import time
import bs4
import urllib.request
import ssl
import pymysql

# 대법원 경매 url 접근 불가 request.text로 가져오기
cookies = {
    "WMONID": "zd4Q2kMgIB0",
    "JSESSIONID": "6Z8QrrFRtjuU5yB17P3Uxp13PsYhdS2vy7xoIaeBie1YDFlBxDz7SGay9VQFlZPt.amV1c19kb21haW4vYWlzMQ==",
    "daepyoSidoCd": "26",
    "daepyoSiguCd": "380",
    "mvmPlaceSidoCd": "",
    "mvmPlaceSiguCd": "",
    "rd1Cd": "",
    "rd2Cd": "",
    "realVowel": "35207_45207",
    "roadPlaceSidoCd": "",
    "roadPlaceSiguCd": "",
    "vowelSel": "35207_45207",
    "toMul": "%BA%CE%BB%EA%BC%AD%BA%CE%C1%F6%BF%F8%2C20220130001238%2C1%2C20230712%2CB%5E",
    "locIdx": "",
    "realJiwonNm": "%BA%CE%BB%EA%BC%AD%BA%CE%C1%F6%BF%F8",
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    # 'Cookie': 'WMONID=zd4Q2kMgIB0; JSESSIONID=6Z8QrrFRtjuU5yB17P3Uxp13PsYhdS2vy7xoIaeBie1YDFlBxDz7SGay9VQFlZPt.amV1c19kb21haW4vYWlzMQ==; daepyoSidoCd=26; daepyoSiguCd=380; mvmPlaceSidoCd=; mvmPlaceSiguCd=; rd1Cd=; rd2Cd=; realVowel=35207_45207; roadPlaceSidoCd=; roadPlaceSiguCd=; vowelSel=35207_45207; toMul=%BA%CE%BB%EA%BC%AD%BA%CE%C1%F6%BF%F8%2C20220130001238%2C1%2C20230712%2CB%5E; locIdx=; realJiwonNm=%BA%CE%BB%EA%BC%AD%BA%CE%C1%F6%BF%F8',
    "Origin": "https://www.courtauction.go.kr",
    "Referer": "https://www.courtauction.go.kr/InitMulSrch.laf",
    "Sec-Fetch-Dest": "frame",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

data = "bubwLocGubun=1&jiwonNm=%BA%CE%BB%EA%BC%AD%BA%CE%C1%F6%BF%F8&jpDeptCd=000000&daepyoSidoCd=26&daepyoSiguCd=380&daepyoDongCd=&notifyLoc=on&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2023&saSer=&ipchalGbncd=000331&termStartDt=2023.06.29&termEndDt=2023.07.13&lclsUtilCd=&mclsUtilCd=&sclsUtilCd=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y"

response = requests.post(
    "https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf",
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)


# ssl_context = ssl.SSLContext()
# ssl_context.verify_mode = ssl.CERT_NONE
caseNo, itemNo, classification, address, link, Appraisal, saleDate = (
    "",
    "",
    "",
    "",
    "",
    "",
    "",
)

null = None


## 함수 선언 부분
def insertData(caseNo, itemNo, classification, address, link, Appraisal, saleDate):
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6, data7 = (
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    )
    sql = ""

    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="mysql",
        database="nateNewsLive",
        charset="utf8",
    )
    cur = con.cursor()
    #    title` VARCHAR(200) NULL,
    #   `publisher` VARCHAR(45) NULL,
    #   `newsDate` VARCHAR(10) NULL,
    #   `newsTime` VARCHAR(6) NULL,
    #   `newsDetail` VARCHAR(200) NULL,
    #   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = caseNo
    data2 = itemNo
    data3 = classification
    data4 = address
    data5 = link
    data6 = Appraisal
    data7 = saleDate
    #
    try:
        print(null)
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        print(data6)
        print(data7)
        sql = (
            "INSERT INTO auctionTable (caseNo, itemNo, classification, address, link,Appraisal,saleDate)  VALUES('"
            + data1
            + "','"
            + data2
            + "','"
            + data3
            + "','"
            + data4
            + "','"
            + data5
            + "','"
            + data6
            + "','"
            + data7
            + "')"
        )
        cur.execute(sql)

    except:
        print("예외 발생")
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else:
        print("성공")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()


##

# nateUrl = "https://news.nate.com/recent?mid=n0100"
while True:
    # htmlObject = urllib.request.urlopen(nateUrl, context=ssl_context)
    # webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(response.text, "html.parser")
    tbody = bsObject.find("tbody")
    trDatas = tbody.findAll("tr")

    print("###### 실시간 뉴스 속보 #######")
    num = 1
    for tdData in trDatas:
        data = tdData.findAll("td")
        caseNo = data[1].text
        itemNo = data[2].text
        classification = data[2].text
        address = data[3].text
        Appraisal = data[5].text
        saleDate = data[6].text
        link = data[4].text

        # insertData(caseNo, itemNo, classification, address, link,Appraisal,saleDate)
        print("(", num, ")", caseNo)
        num += 1

    time.sleep(60)
