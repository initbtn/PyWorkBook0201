answer = 0
startNum = int(input("첫 번째 숫자를 입력하세요 :"))
lastNum = int(input("두 번째 숫자를 입력하세요 :"))
addNum = int(input("더할 숫자를 입력하세요 :"))

for i in range(startNum, lastNum + 1, addNum):
    answer = answer + i

print(" %d+%d+...+%d는 %d입니다." % (startNum, startNum + addNum, lastNum, answer))
