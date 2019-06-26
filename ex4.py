# guess the number
import random 
my_random_number = random.randint(1, 20)
secret = my_random_number
userguess = int(input("What is the secret number?: "))
tries = 0
#loop guess
while (userguess != my_random_number):  
    if (tries == 5):
        break
    print(str(userguess) + "that's not it")    
    if userguess == my_random_number:
        print("You got it!")
    elif userguess > secret:
        print(str(userguess) + "that's too high, try again")
    else:
        print(str(userguess) + "That's too low, try again")
    guess = int(input("Guess again: "))
    tries += 1
