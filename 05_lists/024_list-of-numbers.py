# creating list of numbers

nums = list(range(1,11))
print(nums)

# printing odd numbers
odd_nums = list(range(1,22, 2))
print(odd_nums)

# printing even numbers
even_nums = list(range(0,22, 2))
print(even_nums)

# printing squares
squares = []
for value in range (0,11):
    square = value ** 2
    squares.append(square)
print(squares)

# sum of list elements
nums = list(range(0,101))
sum = sum(nums)
print("Sum of numbers between 0 and 100 is: " + str(sum))