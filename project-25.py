# Collecting Names Using lists V.2
names_list = []
idea = int(input("1. Add a name \n2. Remove a name \n3. Save and Exit :"))

while idea != 3:
    
    if idea == 1 :
        new_name=input("\n>>> New name :")
        names_list.append(new_name)
        idea = int(input("\n1. Add a name \n2. Remove a name \n3. Save and Exit :"))
        
    elif idea == 2 :
        remove=input("\nEnter a name for REMOVE :")
        index=names_list.index(remove)
        del names_list[index]
        print(">>> ",remove," Deleted <<<")
        idea = int(input("\n1. Add a name \n2. Remove a name \n3. Save and Exit :"))

print("\n")
print(names_list)
print(">>> Saved")
