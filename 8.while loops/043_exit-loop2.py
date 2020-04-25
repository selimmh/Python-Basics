# exit from infinite loop v.2
# using flag 

prompt = ("\nTo quit the program, enter 'x'\nEnter your name: ")

flag = True

while flag:
    msg = input(prompt)

    if msg == 'x':
        flag = False
    else:
        print(msg)