'''
Write a python program to find the sum of even number from 0 to 99.
'''
#Method-1
sum = 0

for i in range(0,100):
    if i%2==0:
        sum=sum+i
print(sum)

#Method-2
sum2 = 0
for i in range(0,100,2):
    sum2 = sum2+i
print(sum2)