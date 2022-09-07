#1 ask two integer nummber with user and a function should return their addition:

first = int(input("what is your number: "))
second = int(input("what is your second number: "))

def addition():
    sum = first + second
    print (f"your addition of both number is: { sum }  ")
    return (sum)

addition()

#2 ask an information of your laptop and function should return like this:
# brand_name Model_name price
# eg del vostro @ Rs. 80000

brand_name = input("what is your brand name of your laptop: ")
model_name = input("what is your model name of your laptop: ")
price = int(input("what is the price for your laptop:"))

def informamtion():
    print(f"{brand_name} {model_name} @ Rs. {price }" )

informamtion()



# working model of atm machine: 

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False 

required_amt = int(input("Please enter your amount:"))
print("Please insert your card:")


def read_card():
    card_details=[1200, False,False]
    total_price= card_details[0]
    is_same_bank=card_details[1]
    is_expired=card_details[2]
    if is_expired == False: 
        perform_transactions(total_price, is_same_bank, required_amt)
    else:
        return "Sorry, this card can not be accepted here"

def perform_transactions(total_amt, is_same_bank,required_amt):
    charge = 0
    if not is_same_bank:
        charge = 5
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
           
            print(f"Remaining available balance:{total_amt-required_amt-charge}")
            return required_amt

read_card()

