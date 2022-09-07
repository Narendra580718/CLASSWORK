user_details = int(input("What is your number: "))
dic = []

def user(user_list):
    for num in range(1, user_list+1,1):
        dic.append(num)

user(user_details)
print(f"Your numbers are: {dic}")

user_list = int(input("What is your number: "))
even = []
odd = []

def seperate():
    for i in range(1,user_list+1,1):
        if i %2 ==1:
            odd.append(i)
        else:
            even.append(i)

seperate()
print(f"The even number are: {even}, The odd numbers are: {odd}")

