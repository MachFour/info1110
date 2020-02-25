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
