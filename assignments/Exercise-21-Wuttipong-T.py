from tkinter import *
import math

def leftClickButtton(event):
    x = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    if x >= 30:
        labelresult.configure(text="อ้วนมาก 30.0 ขึ้นไป")
    elif x >= 25 and x <= 29.9:
        labelresult.configure(text = "อ้วน 25.0 - 29.9")
    elif x >= 23 and x <= 24.9:
        labelresult.configure(text = "น้ำหนักเกิน 23.0 - 24.9")
    elif x >= 18.6 and x <= 22.9:
        labelresult.configure(text = "น้ำหนักปกติ 18.6 - 22.9")
    else:
        labelresult.configure(text="ผอมเกินไป น้อยกว่า 18.5")
MainWindow = Tk()
labelHeight = Label(MainWindow,text = "ส่วนสูง")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text ="น้ำหนัก")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButtton)
calculateButton.grid(row=2,column=0)
labelresult = Label(MainWindow,text="ผลลัพธ์")
labelresult.grid(row=2,column=1)
MainWindow.mainloop()