# guess the number
import random 
my_random_number = random.randint(1, 10)
secret = my_random_number
guess = ()
while (guess != my_random_number):
    guess = int(input("What is the secret number?"))
    if guess == my_random_number:
        print("You got it!")
    elif guess > secret:
        print(str(guess) + "that's too high, try again")
    else:
        print(str(guess) + "That's too low, try again")
