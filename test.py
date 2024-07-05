from tkinter import *

root = Tk()
root.title("Test")
root.geometry("500x500")

def test():
    print("Hello World")

button = Button(root, text="Click Me", command=test)
button.pack()

root.mainloop()
