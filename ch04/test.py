from tkinter import *
from tkinter import messagebox


def myFunc():
    messagebox.showinfo("다이얼 로그 제목 줄입니다.!", "다이얼로그 내용 창입니다.")


window = Tk()
window.title("윈도우창 연습")
window.geometry("500x400")
window.resizable(width=True, height=True)
label1 = Label(window, text="문자열1")
label2 = Label(window, text="문자열2", font=("궁서체", 30), fg="red")

photo = PhotoImage(file="GIF/dog.gif")
photo2 = PhotoImage(file="GIF/cat.gif")
photo3 = PhotoImage(file="GIF/cat2.gif")
labelImg = Label(window, image=photo)
labelImg2 = Label(window, image=photo2)
labelImg3 = Label(window, image=photo3)

button1 = Button(window, text="파이썬 종료", fg="red", command=quit)
button1.pack()

button2 = Button(window, image=photo3, command=myFunc)
button2.pack()

labelImg.pack(side=LEFT)
labelImg2.pack(side=RIGHT)
labelImg3.pack()

label1.pack()
label2.pack()

window.mainloop()
