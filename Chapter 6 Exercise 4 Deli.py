sandwich_orders = ["Club Sandwich", "Meatball Sub", "Fried Chicken Sub", "BMT Sandwich"]
finished_sandwiches = []
for x in sandwich_orders:
    if x == ("Club Sandwich"):
        print("The Club Sandwich your asked for is finished.")
    elif x == ("Meatball Sub"):
        print("Your Meatball Sub order is ready.")
    elif x == ("Fried Chicken Sub"):
        print("Here is your Fried Chicken Sub, valued custoomer.")
    else:
        print("Your BMT Sandwich has arrived.")
finished_sandwiches.append(sandwich_orders)
print(*finished_sandwiches)
#Used a for “for” loop and a nested “if-elif” statement to make this code possible and print a specific code for each sandwich. 

#This time I did have to use the “append” command on the twelfth line to add the contents of the “sandwich_orders” list to the  “finished_sandwiches” list. 