# exit from infinite loop v.3
# using break and continue statements

prompt = ("\nType 'x' to exit.\nEnter: ")

while True:

    msg = input(prompt)

    if msg == 'x':
        break
    else:
        continue
