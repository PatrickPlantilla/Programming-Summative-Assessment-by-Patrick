items = [{'code':1, 'item':'500ml Water Bottle', 'price':10},{'code':2, 'item':'330ml Coca Cola Can', 'price':30},{'code':3, 'item':'330ml Pepsi Can', 'price':30},{'code':4, 'item':'330ml Mountain Dew Can', 'price':30},{'code':5, 'item':'330ml Fanta Can', 'price':30},{'code':6, 'item':'330ml Diet Coke', 'price':30},{'code':7, 'item':'330ml Diet Pepsi', 'price':30},{'code':8, 'item':'130ml Lacnor Chocolate Milk', 'price':15},{'code':9, 'item':'130ml Lacnor Strawberry Milk', 'price':15},{'code':10, 'item':'330ml Orange Juice', 'price':20},{'code':11, 'item':'330ml Mango Juice', 'price':20},{'code':12, 'item':'330ml Apple Juice', 'price':20},] #The prices perferctly reflect the current state of inflation in the global economy. Water is now 10 dirhams.
selected_item = int(input(" _____________________________________________________________\n|          Hello this is the liquids Vending Machine!         |\n|       These are the drinks you can get and their price:     |\n---------------------------------------------------------------\n|     (1) Water     |   (2) Coca Cola   |      (3) Pepsi      |\n|     10.00AED      |      30.00AED     |      30.00AED       |\n|-------------------|-------------------|---------------------|\n| (4) Mountain Dew  |     (5) Fanta     |    (6) Diet Coke    |\n|     30.00AED      |      30.00AED     |      30.00AED       |\n|-------------------|-------------------|---------------------|\n|  (7) Diet Pepsi   |(8) Chocolate Milk | (9) Strawberry Milk |\n|     30.00AED      |     15.00AED      |      15.00AED       |\n|-------------------|-------------------|---------------------|\n| (10) Orange Juice | (11) Mango Juice  |  (12) Apple Juice   |\n|     20.00AED      |     20.00AED      |      20.00AED       |\n---------------------------------------------------------------\nEnter the code number of the item you want to get:")) #I made a nice little ascii art to make the terminal more vending machine-looking. 
for x in items:
    if selected_item == x['code']:
        item_bought = x
if item_bought == "":
    print("There is no item which has that code. Please pick between the 12 options.")
else: #This is the main body of the code. The part that inputs money and dispenses the drink.
    print(f"{item_bought['item']} will costs, {item_bought['price']} AED")
    cash_inserted = int(input(f"Enter {item_bought['price']} AED to purchase your drink: "))
    if cash_inserted == item_bought['price']:
        print(f"\n*drops {item_bought['item']}*\nThank you for purchasing a/an {item_bought['item']}. Goodbye :)")
    elif cash_inserted <= item_bought['price']:
        print(f"You have entered an insufficient amount of cash to purchase the item. Please pay with the sufficient ammount and try again.")
    elif cash_inserted >= item_bought['price']:
        print(f"\nYou have entered more than the price of the item. {cash_inserted - item_bought['price']} is your change.\n*drops {item_bought['item']} and drops {cash_inserted - item_bought['price']} AED in change.*\nEnjoy your drink and goodbye :)")