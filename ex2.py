# guess the number
secret = 5
guess = ()
while (guess != secret):
    guess = int(input("What is the secret number?"))
    if guess == 5:
        print("You got it!")
    elif guess > secret:
        print(str(guess) + "that's too high, try again")
    else:
        print(str(guess) + "That's too low, try again")