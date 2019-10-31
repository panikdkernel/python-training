def highestSalary(d):                              #Function definition 
    max=0
    l=[]
    for key,value in d.items():          
        if value>max:      
            max=value                              #Logic for maximum salary
            #g=key
    for key,value in d.items():
        if(value==max):
            l.append(key)
    return l  

a={"Tom":2000,"Ravi":3500,"Ajay":3000,"Aniket":3500}
m=highestSalary(a)                                #Function called
# print(m)
for i in m:
    print(f"Employee {i} has highest salary")
#print(f"{m} is the employee having highest salary of {a[m]}")  #Print details of the Employee with salary    