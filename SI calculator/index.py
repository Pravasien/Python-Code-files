from tkinter import *
window = Tk()
window.geometry("400x350")
Label(window, text="Principal").pack()
principal = Entry(window)
principal.pack()
Label(window, text="rate").pack()
rate = Entry(window)
rate.pack()
Label(window, text="time").pack()
time = Entry(window)
time.pack()
def calc():
    simple_intrest = float(principal.get()) * float(rate.get()) * float(time.get()) / 100
    Label(window, text=simple_intrest).pack()
Button(window, text="Calculate the SI", command=calc).pack()
window.mainloop()