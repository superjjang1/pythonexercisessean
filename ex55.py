# guess the number
import random 
my_random_number = random.randint(1, 20)
secret = my_random_number
tries = 0
play_again = True
while (play_again):
    play_gain = False
    userguess = int(input("What is the secret number?: "))


#loop guess
    while (userguess != my_random_number):  
        if (tries == 5):
            break
            print(str(userguess) + "that's not it")    
        if userguess == my_random_number:
            print("You got it!")
        elif userguess > my_random_number:
            print(str(userguess) + "that's too high, try again")
        else:
            print(str(userguess) + "That's too low, try again")
        userguess = int(input("Guess again: "))
        tries += 1
        
    play = input("would you like to try again? (Y/N)")
    if play.lower() == 'y':
        play_again=True
        tries = 0
        userguess = 0
        my_random_number = random.randint(1,20)
    elif play.lower() == 'n':
        play_again=False
print("thanks")