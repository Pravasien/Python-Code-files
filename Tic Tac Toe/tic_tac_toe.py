Board_Design={"7":" ","8":" ","9":" ",
              "4":" ","5":" ","6":" ",
              "1":" ","2":" ","3":" "
}
board_keys=[]
for key in Board_Design:
    board_keys.append(key)

def printBoard(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-+-+-")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-+-+-")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
def game():
    turn="X"
    count=0
    for i in range(10):
        printBoard(Board_Design)
        print("It's your turn,"+turn+".Move to which place?")
        move=input()
        if Board_Design[move]==" ":
            Board_Design[move]=turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count>=5:
            if Board_Design["7"]==Board_Design["8"]==Board_Design["9"]!=" ":
                printBoard(Board_Design)
                print("\nGame Over. \n")
                print("The winner is ",turn)
                break
            elif Board_Design["4"]==Board_Design["5"]==Board_Design["6"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["1"]==Board_Design["2"]==Board_Design["3"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["1"]==Board_Design["4"]==Board_Design["7"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["2"]==Board_Design["5"]==Board_Design["8"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["3"]==Board_Design["6"]==Board_Design["9"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["7"]==Board_Design["5"]==Board_Design["3"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
            elif Board_Design["1"]==Board_Design["5"]==Board_Design["9"]!=" ":
                printBoard(Board_Design)
                print("\nGame over.\n")
                print("The winner is ",turn)
                break
        if count==9:
            print("\nGame Over.\n")
            print("Its a tie!")
        if turn=="X":
            turn="O"
        else:
            turn="X"
    restart=input("Do you want to play again? (y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            Board_Design[key]=" "
        game()
if __name__=="__main__":
    game()