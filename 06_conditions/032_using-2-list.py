# checking if a value is not in a list

admin_users = ['selim', 'perman']

# ask for username
username = input("Enter username: ")

# check if user is an admin user
if username not in admin_users:
    print("You do not have access")
else:
    print("Welcome to admin panel")
