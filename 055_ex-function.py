# program that keeps looping untill you enter given keyword

def my_function(name, surname):

    full_name = "\nHello " + name.title() + " " + surname.title() + "."
    return full_name

while True:

    print("\nType 'quit' to quit.")

    users_name = input("Your name: ")
    if users_name == 'quit':
        print("...Quitting program...")
        break
    else:
        users_surname = input("Your surname: ")
        if users_surname == 'quit':
            print("...Quitting program...")
            break
        
    print(my_function(users_name,users_surname))