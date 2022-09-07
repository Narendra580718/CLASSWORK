f_name=input("your firsst name is:")
l_name=input("ypur last name is:")
def full_name(first_name, last_name):
    full_name = first_name + last_name
    print(f"your full name is:{first_name} {last_name}")
    return full_name
    

print ("your full name is:", full_name(f_name,l_name))