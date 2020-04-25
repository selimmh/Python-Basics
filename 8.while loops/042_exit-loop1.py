# exit from infinite loop v.1
# simple

prompt = ("\nTo quit the program, enter 'x'\nEnter your name: ")

msg = ""

while msg != 'x':
    msg = input(prompt)
    print(msg)