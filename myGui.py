#from tkinter import *
import tkinter

myText = "Hello World!"

def buttonClicked():
    myText = "Dave says " + textInput.get()
    textOutput.configure(text=myText)

rootWindow = tkinter.Tk()

textOutput = tkinter.Label(rootWindow, text=myText, font=("Arial Bold", 50), fg="Red", bg="Light Gray")
textOutput.pack()
textInput = tkinter.Entry(rootWindow,width=25)
textInput.pack()
buttonOne = tkinter.Button(rootWindow, text="Enter", command=buttonClicked)
buttonOne.pack()
rootWindow.mainloop()