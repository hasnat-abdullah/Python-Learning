tuple1 = ('physics', 'chemistry', 1997, 2000)
tuple2 = ('math', 'biology', 1800)

for item in tuple1:
    print(item)

tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1 * 2)

tuple1_length = len(tuple1) # item count
print(tuple1_length)


is_exist_2000 = 2000 in tuple1 # check an item exist
print(is_exist_2000)

is_not_exist_2000 = 'chemistry' not in tuple1 # check an item exist
print(is_not_exist_2000)

num_tuple = (2, 5, 7, 8, 12, 23, 6)
print(max(num_tuple)) # maximum number
print(min(num_tuple)) # minimum number

print(tuple1[0])
