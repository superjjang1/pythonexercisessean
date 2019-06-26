print("You have 0 coins. Do you want another?")
coin = input("yes or no")
x = 0
while coin.lower() == "yes":
    x += 1
    print("You have " +  str(x) + " coins.")
    coin = input("yes or no")
if coin.lower() == "no":
    print("bye")

    