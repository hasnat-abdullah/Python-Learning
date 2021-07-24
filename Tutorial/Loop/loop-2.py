'''
1+2+3+4......+10=?
'''
import time
start1=time.time()
sum = 0

for i in range(1,9999999):
    sum = sum+i

print(sum)
end1=time.time()
print(f"Executed time for loop- {end1-start1}")

start2= time.time()
sum2 = 9999999*(9999999+1)/2
print(sum2)
end2 = time.time()
print(f"Executed time for equation- {end2-start2}")