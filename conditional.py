#conditional statement in pythom

name = input("what is your name : ")
age = int(input("what is your age? : "))

if age<0:
    print("invalid age")
elif age==10:
    print(f"dear {name}, your ticket price is: 100")
elif age>10:
    print(f"dear {name}, your ticket price is: 150")
else:
    print(f"dear {name}, your ticket price is: 50")
    
