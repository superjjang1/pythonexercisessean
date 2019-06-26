# guess the number as function TT

import random
def guessinggame(): 
    my_random_number = random.randint(1, 20)
    running = True
    while running:
        userguess = int(input("What is the secret number?: "))
        tries = 0
#loop guess
    while (userguess != my_random_number):  
        if (tries == 5):
            break
        again = input(str(userguess) + "that's not it, play again? (y/n)")
        if again == "y" or "Y":
            guessinggame()
        elif again == "n" or "N":
            print("okay. See you next time")
            break
        if userguess == my_random_number:
            print("You got it!")
        elif userguess > my_random_number:
            print(str(userguess) + "that's too high, try again")
        else:
            print(str(userguess) + "That's too low, try again")
    userguess = int(input("Guess again: "))
    tries += 1

guessinggame()
