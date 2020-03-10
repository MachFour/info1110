# Brief overview of if, else, and elif


### Recap: if 
# 'if' on its own is used to execute an action if a certain condition holds,
# otherwise no action is taken. For example:

day = "Monday"
if day == "Monday":
    print("Let's start the week")
# if day is not Monday, nothing happens


### New keyword: else
# 'if' and 'else' are used together to ensure that exactly one of two
# alternative actions are taken, depending on whether the condition is true.

# Example:
test_mark = 75 # percent
pass_mark = 50 # percent
if test_mark > pass_mark:
    print("You passed the test! Congratulations!")
else:
    print("Unfortunately you didn't pass the test.")


### New keyword: elif
# 'elif' can be used to provide more alternatives based on other conditions.
# The conditions for the 'if', 'elif', 'else' statements are checked in order,
# from top to bottom in the code.
# When a condition is found to be True, the corresponding action is taken,
# and after that, no other code from the if/elif/else block is executed.
# As above, 'else' is optional. If 'else' is not used, then it is possible that
# no action will be taken.

# Example:
has_opal_card = False
has_credit_card = True
if has_opal_card:
    # if the condition is true, only this line is executed
    print("Great, you can catch public transport with your Opal Card!")
elif has_credit_card:
    # This line executes if all of the previous if/elif conditions were false
    print("It's okay, you can still use your credit card to tap on.")
else:
    print("Oh no, you can't catch public transport...")

# Any number of 'elif' statements can be used in between 'if' and 'else', but
# 'if' must always be the first one, and when 'else' is used, it must always
# come at the end.

# Example - what does this code output?
secret_number = 420*69
print("I'm thinking of a number, can you guess what it is?")
print("Here's a hint: ", end=" ")
# bonus: we can use end=" " to print something else on the same line
if secret_number > 100:
    print("It's kind of a big number")
elif secret_number > 1000:
    print("It's a big number")
elif secret_number > 10000:
    print("It's a really big number!")

