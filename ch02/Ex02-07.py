import turtle
import random

# 변경기능 : 좌클릭
# 이동 + 선 색 변경(랜덤)+
# 거북이 크기 변경(랜덤) randrange(1,10) 참고 +
# 거북이 회전 (랜덤)+
# 선 굵기 (랜덤) pansize(pSize) 참고, 1-10 사이

## 함수 선언 부분 ##
def  screenLeftClick(x,y):
    tSize = random.uniform(0.1, 2.0)
    pSize = random.randrange(1, 10)
    rAngle = random.randrange(1,360)
    fDistance=random.randint(30,50)
    global r, g, b
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.shapesize(tSize, tSize)
    turtle.pensize(pSize)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.right(rAngle)
    turtle.forward(fDistance)


def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def  screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.register_shape("ch02\elephant.gif")
turtle.title('거북이로 그림 그리기')
turtle.shape("ch02\elephant.gif")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
