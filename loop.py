#even_num_list=[2,4,6,8,10]
#range(s,s,s) --> start , stop, step
for i in range(0,10,1) :
    print(f"The value of i is: {i}") 


days_list = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thrusday" , "Friday" , "saturday"]

for day in days_list:
    print(f"The single day is: {day}")

for num in range(0,10+1,1) :
    if num %2 ==1:
        print(f"The value of num is: {num}")