from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("400x400")
def handle_keypress(event):
  print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
  print("Hi welcome")
button1=Button(window,text="Click Me!",bg="green",fg="black",bd=2)
button1.pack()
button1.bind("<Button-1>",handle_click)
window.mainloop()