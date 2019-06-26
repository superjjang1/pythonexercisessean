print("Total bill amount")
total = int(input(' dollars is your total.'))
print(str(total) + " dollars " + "is your total.")
print("How would you like to split the bill?")
splitA = int(input("split "))
servLvl = input("How was the service? good, fair, or bad?")
if servLvl == "good":
    print("Your total with tip is" + str((int(total) * 20/100 + int(total)) / splitA))
elif servLvl == "fair":
    print("Your total with tip is" + str((int(total) * 15/100 + int(total)) / splitA))
elif servLvl == "bad":
    print("Your total with tip is" + str((int(total) * 10/100 + int(total)) / splitA))




