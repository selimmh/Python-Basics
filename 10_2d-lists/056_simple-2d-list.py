# 2d lists and nested loops

# user enters size of 2d list
m = int(input('V[?][?]: '))
n = int(input('V[' + str(m) + '][?]: '))

print('Matrix size: V[' + str(m) + '][' + str(n) + ']')

matrix = []


for i in range(0,m):
    matrix += [0]


for i in range (0,m):
    matrix[i] = [0]*n

# neseted loop
for i in range (0,m):
    for j in range (0,n):

        matrix[i][j] = int(input('[' + str(i+1) + ':' + str(j+1) + ']: '))

print("\n")

# prints elements of 2d list as grid
for line in matrix:
    for coloumn in line:
        print(coloumn, end=' ')
    print()

