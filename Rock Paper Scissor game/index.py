from tkinter import *
import random
window = Tk()
window.geometry("400x400")
window.title("Rock Paper Scissor Game")
user_choice = ""
def choose(choice):
    global user_choice
    user_choice = choice
def rock():
    choose("Rock")
def paper():
    choose("Paper")
def scissor():
    choose("Scissor")
def play():
    computer = random.choice(["Rock", "Paper", "Scissor"])
    if user_choice=="Rock" and computer=="Rock":
        result="Tie"
    elif user_choice=="Rock" and computer=="Paper":
        result="Computer Wins"
    elif user_choice== "Rock" and computer== "Scissor":
        result="You Win"
    elif user_choice== "Paper" and computer== "Rock":
        result="You Win"
    elif user_choice== "Paper" and computer== "Paper":
        result="Tie"
    elif user_choice== "Paper" and computer== "Scissor":
        result="Computer Wins"
    elif user_choice== "Scissor" and computer == "Rock":
        result="Computer Wins"
    elif user_choice== "Scissor" and computer =="Paper":
        result="You Win"
    elif user_choice== "Scissor" and computer== "Scissor":
        result="Tie"
    Label_Score.config(text="Your chocie ! "+user_choice+" | Computers choice!! "+computer+"the winner is :"+result)
Button_Rock=Button(window,text="Rock",command=rock)
Button_Paper=Button(window,text="Paper",command=paper)
Button_Scissor=Button(window,text="Scissor",command=scissor)
Button_Play=Button(window,text="Play!", command=play)
Label_Score=Label(window,text="Score")
Label_Score.pack()
Button_Rock.pack()
Button_Paper.pack()
Button_Scissor.pack()
Button_Play.pack()
window.mainloop()