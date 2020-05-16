# and condition is useful for cheking multiple conditions

print("...Log in...")

username = input("Enter username: ")
password = input("Enter password: ")

if username == 'selim' and password != 'selim123':
    print("Incorrect password")

elif username != 'selim' and password == 'selim123':
    print("Incorrect username")

elif username != 'selim' and password != 'selim123':
    print("Incorrect username and password")
    
else:
    print("Logged in")
