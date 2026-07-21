import random
lauda= random.choice([1,2,3])
your_input=input("enter your choice(s, p , c): ")
yourdict={"s":1 , "p":2 , "c":3}
reversedict = {1:"s", 2:"p", 3:"c"}
you=yourdict[your_input]
print(f"you chose: {reversedict[you]}\nlauda chose: {reversedict[lauda]}")
if(lauda==you):
    print("draw")
elif(lauda==1 and you==2):
    print("lauda won")
elif(lauda==1 and you==3):
    print("lauda won")
elif(lauda==2 and you==1):
    print("you won")
elif(lauda==2 and you==3):
    print("you won")
elif(lauda==3 and you==1):
    print("you won ")
elif(lauda==3 and you==2):
    print("lauda won")  
else:
    print("invalid input")  

