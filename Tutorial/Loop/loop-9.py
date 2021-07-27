'''
 ----*
 ---**
 --***
 -****
 *****
'''
for row in range(0,5):
    for col1 in range(4,row,-1):
        print("-", end='')
    for col2 in range(0, row+1):
        print("*", end='')
    print()