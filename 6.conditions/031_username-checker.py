# username checker using lists

users = ['user1', 'user2', 'user3']

username = input("Enter yout username: ")

if username in users:
    print("Sorry, username already taken")
else:
    print("Username added to list")
    users.append(username)

print(users)