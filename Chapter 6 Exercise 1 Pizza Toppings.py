print("Enter an topping for the food.")
print("Enter 'quit' when you are finished.")
topping = "\nEnter an topping for the food:"
topping += "\nEnter 'quit' when you are finished."
while True:
    topping1 = input("enter a topping to add:")
    if topping1 =='quit':
        break
    else:
        print("You have added:", topping1)
print("Your pizza is on the way along with the toppings you have selected!")
#I had to use the while loop along with the “true” operator to make this code. 

#I also had to nest an “if-else” statement to meet the requirements of this exercise. 