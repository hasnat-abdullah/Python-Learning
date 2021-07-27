'''
Nested loop
'''

for i in range(0,5): # Outer loop
    print(f'{i}->', end='')

    for j in range(0,5): # Inner loop
        print(i, end='')
    print() # To print new line

print("the program is end.")