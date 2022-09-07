days = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thrusday" , "Friday" , "saturday"]
#index_list=['0',    '1',       '2',         '3',          '4',         '5',       '6']

my_value = days[3]

print(my_value)


#append() method
#--> it is used to insert data into the existing list

days.append("Kasmiday")
print(days)

print("Your recent days")
for day in days:
    
    print(day, end=" ")


#pop()
#--> it is used to eject the last element/item from the list and return to us.
days.pop()
print(days)

#but, if you put value on (x), x will be ejected.