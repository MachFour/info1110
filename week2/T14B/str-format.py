name = 'Iris'
age = 23

# without string formatting
# message = 'Hi ' + name + ', you are ' + str(age) + ' years old.'
# print(message)

# with string formatting:
# in the string to print, replace the variables with braces {}, then use the
# .format() function on that string
print("Hi {}, you are {} years old.".format(name, age))

length = 12.587
print('Length to 2 decimal places: {:.2f}'.format(length))

# padding with zeros:
count = 100
print("The count is {:06d}".format(count))
#       add zero here ^^ width of the whole number
#                       


# general format
# s = "string, with {} characters".format(variable1, variable2)
# print(s)

# Uppercase strings:
# s = "this is a string"
# s_uppercase = s.upper()

# Generally: <string or variable>.<function>()
#                         "{.2f}".format(length)
#                            name.lower()
