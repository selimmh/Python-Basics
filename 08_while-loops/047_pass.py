# using pass statement

num = 0

for num in range(10):
    if num == 5:
        # loop passes from here
        pass    

    print(str(num))

print('Out of loop')