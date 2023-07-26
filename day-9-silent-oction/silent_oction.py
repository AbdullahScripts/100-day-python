import os
from art import logo
flag_value=False
name_of_user=''
print(logo)
highest=0
users={}
while flag_value==False:
    
    name=input('please enter your name: ')

    price=input('please enter your bid:$')

    users[name]=price

    terminat=input('is there any other person to bid yes or no? ').lower()
    os.system('cls||clear')
    if terminat=='no':
        flag_value=True


for user in users:
    priceH=users[user]
    user_price=int(priceH)
    if user_price>highest:
        highest=user_price
        name_of_user=user
print(f' {name_of_user} won the bid\n his bid was {highest}')




















