'''
loop with conditions
'''

number1= int(input("Enter Start point: "))
number2= int(input("Enter end point: "))

sum = 0

for i in range(number1, number2):
    sum= sum+i

print(f"the sum is {sum}")

if sum>100:
    print("Worng input")
else:
    print("Its ok")