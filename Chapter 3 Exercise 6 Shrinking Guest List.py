NotableFilipinoFigures = ["Jose Rizal", "Andres Bonifacio", "Manuel Quezon", "Ferdinand Marcos Sr."]
for x in NotableFilipinoFigures:
    print("\n\n\nGreetings,", x, "\t\nI would like to invite you to Dinner consisting of many Modern Filipino Cuisine to get your opinion on the state of our nation while having dinner. I would also like to know if the modern renditions of your actions reflect what actually happened.")
print("\n\n\nI have Just been informed that Manuel Quezon cannot join as he is busy fighting in the war.")
del NotableFilipinoFigures[2]
NotableFilipinoFigures.append("Corazon Aquino")
for y in NotableFilipinoFigures:
    print("\n\n\nGreetings,", y, "\t\nI would like to invite you to Dinner consisting of many Modern Filipino Cuisine to get your opinion on the state of our nation while having dinner. I would also like to know if the modern renditions of your actions reflect what actually happened.")
print("\n\n\nThis just in: Unfortunately, I can only invite two people for dinner due to lack of dinner table space.")
remove1 = (NotableFilipinoFigures.pop(1))
print("\n\n\n\nI'm sorry", remove1, "but we do not have enough space to accomodate you.")
remove2 = (NotableFilipinoFigures.pop(2))
print("I'm sorry", remove2, "but we do not have enough space to accomodate you.")
print("\n\n\nGreetings Jose Rizal,\n\t I would like to inform you that you are still invited to join me and Ferdinand Marcos Sr. for dinner.")
print("\nGreetings Ferdinand Marcos,\n\t I would like to inform you that you are still invited to join me and Jose Rizal for dinner.")
del NotableFilipinoFigures[0]
del NotableFilipinoFigures[-1]
print(NotableFilipinoFigures)
#This one was a bit more complicated. While I again still used the same for loop structure, I also added a lot more stuff. Especially the “pop” function. I also used “\n” more extensively in this exercise. 