age = int(input("Enter your age"))
if(age >=0 and age <= 18):
    print("Minror")
    if age > 13:
        print("Childu")
    else:
        print("teenage")
elif (age > 18 and age <= 100):
    print("Adult")
    if age > 60:
        print("Senior Citizen")
    else:
        print("Working Adults")
else:
    print("Invalid age entered")