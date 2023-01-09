rivers = {'Nile' : 'Egypt', 'Amazon': 'Brazil', 'Dneiper': 'Ukraine'}

for key in rivers:
    if key == ('Nile'):
        print("The Nile is the longest river in the World.")
    elif key == ('Amazon'):
        print("The Amazon River is hidden deep inside of the Amazon rainforest.")
    else:
        print("The Dneiper River is pronounced, 'Dnipro.'")

print("\t")
for key in rivers.keys():
    print(key)

print("\t")
for value in rivers.values():
    print(value)
#I chose 5 rivers on the top of my head and i used 3 for loops throughout the code. Each code meets the requirements for all the bulletpoints of this exercise.