
phn = input("Enter your phn number")

if phn.isdigit():
    print('valid phn number')
elif phn[0]=='+' and phn[1:].isdigit():
    print('valid phn number')
else:
    print('phn number not valid')
