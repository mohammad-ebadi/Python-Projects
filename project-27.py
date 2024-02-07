# Collecting Names Using lists & Dictionary 
l=[]

while True:
    name = input("Name : ")
    if name == "0":
        break
    age = input("Age : ")
    city = input("City : ")
    
    d={}
    d["Name"] = name
    d["Age"] = age
    d["City"] = city
    
    l.append(d)

print("------------------") 

for item in l:
    for key in item:
        print(key ,":", item[key])
        
print("\n------------------")
