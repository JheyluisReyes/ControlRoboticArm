import tkinter
from tkinter import *
from time import sleep
import tkinter.messagebox
from pyfirmata import Arduino, util, SERVO

board = Arduino('COM3')
sleep(5)

pinS1 = 2 #Base
pinS2 = 3 #Forearm
pinS3 = 4 #Arm
pinS4 = 5 #Gripper

board.digital[pinS1].mode = SERVO
board.digital[pinS2].mode = SERVO
board.digital[pinS3].mode = SERVO
board.digital[pinS4].mode = SERVO

def servo(positions1):
    board.digital[pinS1].write(positions1)

def servo1(positions2):
    board.digital[pinS2].write(positions2)

def servo2(positions3):
    board.digital[pinS3].write(positions3)

def open():
    board.digital[pinS4].write(90)

def close():
    board.digital[pinS4].write(0)

def info():
    tkinter.messagebox.showinfo("Information", "How to use: The knobs allow you to interact with the Robot's joints and the buttons allow you to interact with the Robot's grippers.")

root = Tk()
root.title("Robotic Arm Control")
root.minsize(800,600) #800,450

img = PhotoImage(file = "images\sample.png")
widget = Label(root, image = img)
widget.grid(column = 1, row = 1)

var = StringVar()
tag = Label(root, textvariable = var, relief = FLAT, pady = 5)
var.set("")
tag.grid(column = 2, row = 1)

var2 = StringVar()
secondtag = Label(root, textvariable = var2)
var2.set("")
secondtag.grid(column = 2, row = 7)

var3 = StringVar()
thirdtag = Label(root, textvariable = var3)
var3.set("")
thirdtag.grid(column = 2, row = 5)

angle = Scale(root, command = servo, from_= 30, to = 150, orient = HORIZONTAL, length = 300, troughcolor = 'gray', width = 30, cursor = 'dot', label = 'Base Position')
angle.grid(column = 2, row = 2)

secondangle = Scale(root, command = servo1, from_ = 100, to = 179, orient = HORIZONTAL, length = 300, troughtcolor = 'gray', width = 30, cursor = 'dot', label = 'Arm Position')
secondangle.grid(column = 2, row = 3)

thirdangle = Scale(root, command = servo2, from_ = 70, to = 179, orient = HORIZONTAL, length = 300, troughcolor = 'gray', width = 30, cursor = 'dot', label = 'Forearm Position')
thirdangle.grid(column = 2, row = 4)

ButtonOpen = Button(root, text = "Open Gripper.", command = open, relief = RAISED, activebackground = 'green', bd = 3, height = 2, width = 17)
ButtonOpen.grid(column = 2, row = 6)

ButtonClose = Button(root, text = "Close Gripper", command = close, relief = RAISED, activebackground = 'red', bd = 3, height = 2, width = 17)
ButtonClose.grid(column = 2, row = 8)

ButtonInfo = Button(root, text = "How to use", relief = GROOVE, COMMAND = info)
ButtonInfo.grid(column = 1, row = 2)

root.mainloop()