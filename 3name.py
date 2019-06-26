print("Hello, please enter three names.")
name1 = input("What's the first name?")
name2 = input("What's the second name?")
name3 = input("What's the third name?")
x = int(len(name1))
y = int(len(name2))
z = int(len(name3))
if x < (y) and (z):
    print("Hello " + name1)
elif y < (x) and (z):
    print("Hello " + name2)
elif z < (y) and (x):
    print("Hello " + name3)
 