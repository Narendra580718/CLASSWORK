'''
It always represent in the form of:
my_dictionary = {"key":"value"} 
'''
#Why we need dictionary?
#---> TO overcome the problem exist in the list.
#for eg:

#user_details = ["kasmi", "Thapa", 20,["English","Nepali","Japnese"],98184152,["Burger", "Pizza", "MOMO"]]

user_details = {
    "first_name":"kasmi",
    "last_name":"Thapa",
    "language_spoken":["English","Nepali","Japnese"],
    "contact":98184152,
    "fav_food":["Burger", "Pizza", "MOMO"]
}

print(user_details["first_name"])




for key,value in user_details.items():
    print(f"The key is:{key} and its value is: {value}")

for key in user_details.keys():
    print(f"The key is:{key} ")

for value in user_details.values():
    print(f" its value is: {value}")