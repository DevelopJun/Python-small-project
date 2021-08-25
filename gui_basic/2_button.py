from tkinter import *

root = Tk()
root.title("June GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

# root.geometry("640x480") # 가로 * 세로
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

# root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
