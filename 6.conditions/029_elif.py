# elif statement is used for more than 2 conditions
# it is quarantine time and going out is tightened

age = input("Enter your age: ")

if int(age) < 18:
    print("You can go outside between 18-20")
elif int(age) > 65:
    print("You can go outside between 11-13")
else:
    print("You can go out whenever you want")