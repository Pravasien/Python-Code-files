from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window=Tk()
window.title("Codingal's Text Editor")
window.geometry("600x600")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
T1=Text(window)
F1=Frame(window,relief=GROOVE,bd=1)
def open():
  filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
  if not filepath:
    return
  T1.delete(1.0, END)
  with open(filepath, "r") as file:
    content = file.read()
    T1.insert(END, content)
  window.title("Codingal's Text Editor - " + filepath)
def save():
  filepath = asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
  if not filepath:
    return
  with open(filepath, "w") as file:
    content = T1.get(1.0, END)
    file.write(content)
  window.title("Codingal's Text Editor - " + filepath)
Button_Open=Button(F1,text="OPEN",command=open)
Button_Save=Button(F1,text="SAVE AS...",command=save)
Button_Open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
Button_Save.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
F1.grid(row=0,column=0,sticky="ns")
T1.grid(row=0,column=1,sticky="nsew")
window.mainloop()