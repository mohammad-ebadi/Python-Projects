# Collecting Names Using lists
name = "pass"
name_list = []
count = 0
while name != "":
    name = input(">>> Enter you're Name OR  >>> For Continue press (ENTER) bottom : ")
    count = count + 1
    if name == "":
        break
    else:
        name_list.append(name)
    
print(">>> Changs saved  <<< Members Name(s) and Count : ","(",count-1, ")",name_list)

####################################

idea = ""
while idea != 3:
    idea = int(input("### ADD a NEW NAME press(1):\n### REMOVE a NAME press(2):\n### SAVE and EXITE press(3):"))

    if idea == 2:
        
        remove = input("\nEnter you're name for remove :")
        if remove not in name_list:
            print(">>> ",remove," Not Found !!!")
        else:
            index = name_list.index(remove)
            del name_list[index]
            print(remove," # Deleted #")
        
        
    elif idea == 1:
        
        name = input(">>> Enter you're Name OR  >>> For Continue press (ENTER) bottom : ")
        
        if name == "":
            break
        
        else:
            name_list.append(name)
        

print(">>> Changs saved  <<< Members Name(s) and Count : ","(",count-1, ")",name_list)
