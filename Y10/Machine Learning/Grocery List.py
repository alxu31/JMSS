#Changes the value into a printable version for the grocery list.
def tick_or_not(tick_untick):
    if tick_untick == "untick":
        return "☐"
    if tick_untick == "tick":
        return "☑"

grocery_list = {}
valid_answers = ["add", "remove", "print", "quit", "tick", "untick"]

#Asks the user what they want to do with the grocery list until they choose to quit.
while True:
    answer = input("Menu(add, remove, print, quit, tick, untick): ")

    #Adds an item of the user's choice to the grocery list/increases the amount if already in the list.
    if answer == valid_answers[0]:
        add_item = input("Item to add: ")
        if len(add_item) > 25:
            #Tells the user the item does not fit on the list.
            print("Sorry that item is too long")
        else:
            if add_item not in grocery_list:
                grocery_list[add_item] = [0,"0"]
                grocery_list[add_item][0] = 1
                grocery_list[add_item][1] = "untick"
            else:
                grocery_list[add_item][0] += 1

            #Ensures ticked items stay ticked.
            if grocery_list[add_item][1] == "tick":
                continue
            else:
                grocery_list[add_item][1] == "untick"
    #Decreases the amount of an item/removes it from the grocery list if there is only one.
    elif answer == valid_answers[1]:
        remove_item = input("Item to remove: ")
        if remove_item in grocery_list.keys():
            if grocery_list[remove_item][0] > 1:
                grocery_list[remove_item][0] -= 1
            else:
                grocery_list.pop(remove_item)
        else:
            #Tells the user the item is not on the list.
            print("That item is not on the grocery list.")

    #Prints the grocery list, including the amount of each item and whether it has been ticked off or not.
    elif answer == valid_answers[2]:
        if grocery_list != {}:
            print("""
---------Grocery List---------
""")
            for key, value in grocery_list.items():
                full_length = 27
                key_length = len(key)
                value_length = len(str(value[0]))
                space_length = full_length - (key_length + value_length)
                print(tick_or_not(value[1]) + " " + str(key) + str(space_length*" ") + str(value[0]))
            print("""
------------------------------
""")

        else:
            print("No items yet")

    #Breaks the while loop, ending the program.
    elif answer == valid_answers[3]:
        break

    #Ticks an item.
    elif answer == valid_answers[4]:
        tick_item = input("Item to tick: ")
        if tick_item not in grocery_list:
            print("That item is not in the list.")
        else:
            grocery_list[tick_item][1] = "tick" 
    #Unticks an item.
    elif answer == valid_answers[5]:
        untick_item = input("Item to untick: ")
        if untick_item not in grocery_list:
            print("That item is not in the list.")
        else:
            grocery_list[untick_item][1] = "untick"

    #Tells the user their input is not an option.
    elif answer not in valid_answers:
        print("Sorry, that input is not valid. Try again.")









