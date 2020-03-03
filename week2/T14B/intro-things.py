
############################
# Some introductory things #
############################

#
# Datatypes:
#    These should be familiar! What is the type of each variable?

count = 10
name = "Alexander the Great"
ratio = 2.3
cost = count*ratio # what datatype is the product of these two variables?

# A new datatype: Boolean! It takes only two values, True and False.
success = True
finished_yet = False

# Variable names:
#    We want to have some basic rules for how we choose variable names:
#    - generally stick to lower case letters
#    - can't start a variable name with a number
#    - replace spaces in words by underscores: '_'
#    - variables named in all uppercase are constants (don't change during the
#      program's execution), e.g. MAX_CAPACITY = 1000
#    - can't (don't) use a name that already means something in python, e.g.
#      print, True, class, if

#    Have a look at the lab sheet and decide whether the variables there are
#    good variable names or not.

#    Further reading on python's variable naming conventions:
#    https://www.python.org/dev/peps/pep-0008/


# 
# Some style points:
#

# 1. Use comments to explain things about your code that are not obvious
#    For example:
radius = 10 # centimetres
area = radius*3.1415*3.1415 # multiply by pi squared


# 2. Try to pick variable names that describe the purpose of the variable
#    We can improve on the previous example:
radius_cm = 10 # now the variable name describes the unit too!
PI = 3.1415 # I used capitals for PI since it's a constant
area_cm_squared = radius_cm*PI*PI



# 3. Don't 'reuse' variables'
#    The following is not very good style:
age = input("What is your age? ")
age = int(age) # this changes age from a string to an int - not good!

# Here is a better way:
age_input = input("What is your age? ") # use a more specific variable name
age = int(age_input) # this one is 'age' because we want to use it as an int

# PEP 8 also has information on good style (in Python)
#    https://www.python.org/dev/peps/pep-0008/
