# guess the number
secret = 5
guess = ()
while (guess != secret):
    guess = int(input("What is the secret number?"))
    if guess == 5:
        print("You got it!")
    else:
        print("try again.")
