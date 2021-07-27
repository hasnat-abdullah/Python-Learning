'''
1
13
135
1357
13579
'''
for i in range(1,6):
    for j in range(1,i*2):
        if j%2!=0:
            print(j, end='')
    print()