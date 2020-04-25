# exit from infinite loop v.2
# using flag 

prompt = ("\nType 'x' to exit.\nEnter: ")

flag = True

while flag:
    msg = input(prompt)

    if msg == 'x':
        flag = False
    else:
        print(msg)
