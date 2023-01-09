print("Hello, you are about to purchase a ticket for Shrek 5 online which is in theaters now!")
age = int(input("Enter your age: "))
while True:
    if age < 3:
        print("You can Shrek 5 for free!")
    elif age >= 3 and age <= 12:
        print("Ticket price to watch Shrek 5 is $10.")
    else:
        print("Ticket price to watch Shrek 5 is $15.")
    break
#This code was pretty easy for me since I basically just had to rewrite the words from a lot of the previous exercises we had to do in class. 

#Used the “while True:” statement like in the first exercise of this chapter and I had to use comparison/relational operators to make this code work. 