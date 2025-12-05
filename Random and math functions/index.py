import random
playing=True
Num_Gen=random.randint(10,20)
while playing:
    guess=int(input("Guess a number between 10 and 20:"))
    if guess==Num_Gen:
        print("congratulations! You have guessed the correct number.")
        playing=False
        break
    elif guess<Num_Gen:
        print("Your guess is too low.Try again.")
    else:
        print("Your number is too high. Try again.")