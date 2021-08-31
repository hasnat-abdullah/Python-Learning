def func_name (x):
    # do something
    return 2*x

def sum(x,y):
    return x+y

print(sum(2,3))

def is_divisible_by_two(x):
    return x%2==0

num = int(input("Enter a number to check: "))
print(is_divisible_by_two(num))

def print_a_song():
    lyrics = "test song test"
    print(lyrics)

print_a_song()

for i in range(0,11):
    if is_divisible_by_two(i):
        print(i)