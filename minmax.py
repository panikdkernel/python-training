#Min and max
l=[]                                             #Declaration of empty list
for i in range(5):                               #Taking user input
    l.append(int(input("Enter no")))
l.sort()                                         #List Sorting in ascending order
print(f"Largest number in the list is {l[-1]}")  #Maximum from the list
print(f"Smallest number in the list is {l[0]}")  #Minimum from the list

                