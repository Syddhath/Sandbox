name = input("Enter your name")
if not name:
    print("You did not enter a name")
else:
    print("Hello",name)
name_1 = name[1::2]
print(name_1)