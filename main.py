#variant = 11 % 4 = 3

height = int(input())

for i in range(height):
    for j in range(i+1):
        print(j+1, end="")
    print('\n')