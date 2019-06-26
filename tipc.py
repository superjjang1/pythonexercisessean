print("Here's the check for your meal.")
total = int(input(' dollars is your total.'))
servLvl = input("How was the service? good, fair, or bad?")
if servLvl == "good":
    print("Your tip amount is" + str(int(total) * 20/100))
elif servLvl == "fair":
    print("Your tip amount is" + str(int(total) * 15/100))
elif servLvl == "bad":
    print("Your tip amount is" + str(int(total) * 10/100))
