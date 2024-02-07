# If the text was more than a certain character , cut it
def string (text):
    if len(text) >10 :
        print("Over 10 char")
        return print(text[0:10])
    else:
        print("less than 10 char")
        print(text)
        
text=input("Enter a text :")
string(text)
