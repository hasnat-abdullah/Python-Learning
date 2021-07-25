start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

if start !=0 and end != 100:
    print("Wrong input")
    exit()

sum = 0
for i in range(0,100):
    sum = sum+i
print(sum)