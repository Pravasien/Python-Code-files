from tkinter import *
window=Tk()
window.geometry("350x400")
window.title("Password Strength Checker App")
numbers=["1","2","3","4","5","6","7","8","9","0"]
letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
symbols=["!","@","#","$","%","^","&","*","(",")"]
def password_Strength_Check():
    password=Entry_Password.get()
    has_num=False
    has_letter=False
    has_symbol=False
    for i in password:
        if i in numbers:
            has_num=True
        if i in letters:
            has_letter=True
        if i in symbols:
            has_symbol=True
    if len(password) > 8 and has_num and has_letter and has_symbol:
        Label(window, text="Your password is really good").pack()
    elif (has_num and has_letter)or(has_num and has_symbol)or(has_letter and has_symbol):
        Label(window,text="Your password is good").pack()
    else:
        Label(window,text="Your password is bad").pack()
Entry_Password=Entry(window)
Entry_Password.pack()
Button_Strength_Checker=Button(window, text="Check your password's strength", command=password_Strength_Check)
Button_Strength_Checker.pack()
window.mainloop()