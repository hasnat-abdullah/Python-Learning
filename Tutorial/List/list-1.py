list1 = ['physics', 'chemistry', 1997, 2000]
list2 = ['math', 'biology', 1800]

for item in list1:
    print(item)

list3 = list1+list2
print(list3)
print(list1*2)

list1[0]='CSE' # update value
print(list1)

list1_length = len(list1) # item count
print(list1_length)

is_exist_2000 = 2000 in list1 # check an item exist
print(is_exist_2000)

is_not_exist_2000 = 'chemistry' not in list1 # check an item exist
print(is_not_exist_2000)

num_list = [2,5,7,8,12,23,6]
print(max(num_list)) # maximum number
print(min(num_list)) # minimum number

num_list.append(50)
print(num_list)

num_list.sort()
print(num_list)

del list1[0] # Delete an object in list
print(list1)