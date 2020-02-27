# Original version from lab sheet
# Take an item from the location
if user_input_splitted[0] == "take":
    # Check item is in this location
    item_to_be_taken = get_obj(user_input_splitted[1], goose.location.items)
    if item_to_be_taken == None:
        print("You don't see anything like that here.")
    else:
        goose.take(item_to_be_taken)
        goose.location.remove_item(item_to_be_taken)
        print("You pick up the {}.".format(item_to_be_taken.item_name))
        chaser_take_action()


#Max's 'super easy to read' version

# determine action from user input and act accordingly
action = user_input_split[0]
if action == "take":
    # First, check item is in this location
    item_name = user_input_split[1]
    current_location = goose.location
    items_at_current_location = current_location.items
    # the variable below will be None if the item is not found
    item_if_found = get_obj(item_name, items_at_current_location)
    if item_if_found is None:
        # the item doesn't exist at the current location; we can't do anything
        print("You don't see anything like that here.")
    else:
        item = item_if_found # new variable name, because it is found
        goose.take(item)
        current_location.remove_item(item)
        print("You pick up the {}.".format(item.name))
        # proceed to the next event in the program
        chaser_take_action()

