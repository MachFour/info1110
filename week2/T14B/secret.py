
secret_value = "secret"

user_input = input("Type in the secret to enter: ")

if user_input == secret_value:
    print("You have entered the correct password!")
if user_input != secret_value: # 'not equals' operator
    print("Wrong password")

#could also use 'else:'
