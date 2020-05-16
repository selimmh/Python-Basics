# using break statement

num = 0

for num in range(10):
    if num == 5:
        # loop breaks here
        break    

    print(str(num))

print('Out of loop')