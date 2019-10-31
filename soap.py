a=[("pears",500),("Lifebuoy",200),("Dettol",700),("Dove",200)] 
d={}
soap=[]
quantity=[]
for i in a:
    j=list(i)
    soap.append(i[0])                               #Form list with product name
    quantity.append(i[1])                           #Form list with product quantity
#print(soap)
#print(quantity)
for key,val in zip(soap,quantity):                  #Formation of dictionary                     
    d[key]=val
print(d)
print("Qauntity of dove is"+str(d["Dove"]))         #Finding quantity with value=Dove
d.pop("Lifebuoy")
print(d)                                            #Removed the item with product name Lifebuoy 
 

    