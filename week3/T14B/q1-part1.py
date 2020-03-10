num = int(input("Enter a number: "))

num = 10 
if num % 2 == 0: 
    num /= 2 
    num = int(num/2) # better (keeps int type)
else:
    #pass # this is the same as no 'else'
    num = 3*num + 1

print(num)
